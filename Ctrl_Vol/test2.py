from pycaw.pycaw import AudioUtilities
sessions = AudioUtilities().GetAllSessions()
for session in sessions:
    if session.Process:
        print(f"{session.Process.name()}")