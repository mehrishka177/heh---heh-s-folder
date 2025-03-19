from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

users = {}
rooms = {"general": set()}  # Начальная комната
log_file = "chat_log.txt"

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    sid = request.sid
    users[sid] = {"username": f"User{len(users) + 1}", "room": "general"}
    join_room("general")
    rooms["general"].add(sid)
    emit('user_count', {'count': len(users)}, broadcast=True)
    emit('user_joined', {'username': users[sid]['username'], 'room': 'general'}, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    sid = request.sid
    if sid in users:
        room = users[sid]['room']
        rooms[room].discard(sid)
        emit('user_left', {'username': users[sid]['username'], 'room': room}, broadcast=True)
        del users[sid]
    emit('user_count', {'count': len(users)}, broadcast=True)

@socketio.on('message')
def handle_message(data):
    sid = request.sid
    username = users[sid]['username']
    room = users[sid]['room']
    timestamp = datetime.now().strftime('%H:%M:%S')
    formatted_msg = f"[{timestamp}] {username}: {data['message']}"
    print(f"Message: {formatted_msg}")
    log_message(formatted_msg)
    send({'text': formatted_msg, 'user': username}, room=room)

@socketio.on('reply')
def handle_reply(data):
    sid = request.sid
    username = users[sid]['username']
    room = users[sid]['room']
    response = "Да" if data['answer'] == 'yes' else "Нет"
    formatted_msg = f"{username} ответил: {response}"
    print(f"Reply: {formatted_msg}")
    log_message(formatted_msg)
    send({'text': formatted_msg, 'user': username}, room=room)

@socketio.on('change_username')
def change_username(data):
    sid = request.sid
    new_username = data['username']
    old_username = users[sid]['username']
    users[sid]['username'] = new_username
    emit('username_changed', {'old_username': old_username, 'new_username': new_username}, broadcast=True)

@socketio.on('join_room')
def handle_join_room(data):
    sid = request.sid
    new_room = data['room']
    old_room = users[sid]['room']
    leave_room(old_room)
    rooms[old_room].discard(sid)
    join_room(new_room)
    users[sid]['room'] = new_room
    if new_room not in rooms:
        rooms[new_room] = set()
    rooms[new_room].add(sid)
    emit('room_changed', {'username': users[sid]['username'], 'new_room': new_room}, broadcast=True)

@socketio.on('send_file')
def handle_file(data):
    filename = data['filename']
    file_content = data['file']
    room = users[request.sid]['room']
    emit('receive_file', {'filename': filename, 'file': file_content}, room=room)

# Логирование сообщений
def log_message(msg):
    with open(log_file, "a") as f:
        f.write(msg + "\n")

if __name__ == '__main__':
    if not os.path.exists(log_file):
        open(log_file, 'w').close()
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)