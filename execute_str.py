import re

def execute_str(problems):
  error = 'False'
  
  if len(problems) > 5:
    error = 'Error: Too many problems.'
  
  else:
    for problem in problems:
      if bool(re.match('(\S*)(\s?)[+-](\s?)(\S*)$', problem)) == False:
        error = "Error: Operator must be '+' or '-'."

      elif bool(re.match('^(\d*)(\s*)([+-])(\s*)(\d*)$', problem)) == False:
        error = 'Error: Numbers must only contain digits.'
        
      elif bool(re.match('^(\d{1,4})(\s*)([+-])(\s*)(\d{1,4})$', problem)) == False:
        error = 'Error: Numbers cannot be more than four digits.'

  return error