import bot_logic.command_functions as comFunc

commandHandler = {
  "inspiro": comFunc.get_inspiro_pic,
  "random": comFunc.random,
  "test": comFunc.get_test,
  "jn": comFunc.get_yes_or_no
}

functions = {
  'right_channel': comFunc.right_channel,
}