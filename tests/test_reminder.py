from lib.reminder import Reminder

def test_reminds_the_user_to_do_a_task():
    reminder = Reminder("Sylwia")
    reminder.remind_me_to("Jibble in")
    result = reminder.remind()
    assert result == "Sylwia, Jibble in!"