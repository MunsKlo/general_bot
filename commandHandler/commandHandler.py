import bot_logic.command_functions as comFunc

commandHandler = {
  "inspiro": comFunc.get_inspiro_pic,
  "random": comFunc.random,
  "test": comFunc.get_test,
  "jn": comFunc.get_yes_or_no,
  "members": comFunc.get_all_members,
  "users": comFunc.get_users,
  "vid": comFunc.get_youtube,
  "help": comFunc.get_commands,
  "@": comFunc.make_important_message
}