import os
from random import randint

# OBFUSCATOR
# Works:
#
# Adds junk code to obfuscate code flow.
# intensio_obfuscator -i source -o test_build -mlen lower -ind 2 -ps
#
# Change filenames.
# intensio_obfuscator -i source -o test_build -mlen lower -ind 2 -rfn
#
# Replaces everything with a string an run using 'exec'.
# intensio_obfuscator -i source -o test_build -mlen lower -ind 2 -rth
#
#
# Kinda works, requires manual fixing of some syntax errors, but it's not a big deal.
# intensio_obfuscator -i source -o test_build -mlen lower -ind 2 -rts

if __name__ == '__main__':
  source_path: str = 'source'
  build_path: str = 'build'
  build_key: str = '7qg3t9hsgd0qk3r=0-qjfg[pjvo88jwav8ehflwn3nrwpfueh'

  # Removes old build folder.
  try:
    os.system('rm -r ' + build_path)
  except:
    print('[*] Current directory is clean of the build folder.')

  # Scripts.
  scripts: list = []

  # Find every .py file.
  for root, dirs, files in os.walk(source_path):
    for file in files:
      if file.endswith('.py'):
        scripts.append(root + '/' + file)
  
  # The source tree.
  source: dict = {}

  # Classes.
  classes: dict = {}

  for script in scripts:
    # Register a class.
    class_name: str = script.split('/')[-1].title()[:-3]
    classes[class_name] = {
      'name': class_name,
      'path': script.split('/', 1)[1],
      'path_in_code': (script.replace('/', '.')[:-3])[len('source.'):],
      'ref': [],
      'name_obf': None
    }

    # Script which is safe to compile.
    clean_script: list = []

    # Builds the 'clean_script' object.
    with open(script) as f:
      lines: list = f.readlines()

      for line in lines:
        # Determines if a line of code will be included into source for build.
        line_is_safe: bool = True

        # Does not allow logging to pass into build.
        if 'logging.debug' in line:
          line_is_safe = False
        if 'logging.info' in line:
          line_is_safe = False
        if 'logging.warning' in line:
          line_is_safe = False
        if 'logging.error' in line:
          line_is_safe = False
        if 'logging.critical' in line:
          line_is_safe = False
        if 'logging.log' in line:
          line_is_safe = False
        if 'logging.exception' in line:
          line_is_safe = False
        
        # If our checks are passed, append a line.
        if line_is_safe == True:
          clean_script.append(line)

    # Adds a 'clean_script' into the source three.
    source[script] = clean_script
  
  # Find import references.
  for script in scripts:
    with open(script) as f:
      lines: list = f.readlines()
      for line in lines:
        for c in classes:
          import_reference: str = 'from ' + classes[c]['path_in_code'] + ' import ' + classes[c]['name']
          if line.startswith(import_reference):
            classes[c]['ref'].append(script)

  # Create a build folder.
  os.system('mkdir ' + build_path)

  #print(classes)

  # Write the source three to new build folder.
  for script in source:
    # Name of a new script.
    file_name: str = build_path + '/' + script.split('/', 1)[1]
    # File path of that new script.
    file_path: str = ''
    for e in file_name.split('/'):
      if not e.endswith('.py'):
        file_path += e + '/'

    # Create a script's directory.
    try:
      os.system('mkdir -p ' + file_path)
    except:
      pass

    # Writes a script.
    with open(file_name, 'w') as f:
      for line in source[script]:
        f.write(line)
    
    # Obfusacate and minify.
    #os.system('pyminifier -o ' + file_name + ' ' + file_name)
    #if script.endswith('env.py'):
    #  os.system('pyminifier -o ' + file_name + ' ' + file_name)
    #else:
    # os.system('pyminifier -o ' + file_name + ' ' + file_name) 

  # os.system('python3 -OO -m PyInstaller --key ' + build_key + ' --onefile ' + build_path + '/main.py')

  # os.system('mv dist/main build/main')
  # os.system('mv main.spec build/main.spec')
  # os.system('rm -r dist')
  
  #os.system('mv main.build ' + build_path + '/main.build')
  #os.system('mv main.dist ' + build_path + '/main.dist')

  #for c in classes:
  #  for ref in classes[c]['ref']:
  #    ref = build_path + '/' + ref.split('/', 1)[1]
  #    #print(c, ref)
  #    with open(ref) as f:
  #      lines: list = f.readlines()
  #      for line in lines:
  #        if line.startswith('class '):
  #          print(c, ref, line)

  # Grab obfuscated name.
  #for c in classes:
  #  with open(build_path + '/' + classes[c]['path']) as f:
  #    lines: list = f.readlines()
  #    for line in lines:
  #      if line.startswith('class '):
  #        classes[c]['name_obf'] = line[6:][:-2]
  
  #for c in classes:
  #  for ref in classes[c]['ref']:
  #    ref = build_path + '/' + ref.split('/', 1)[1]
  #    #print(c, ref)

  #    updated_lines: list = []

  #    with open(ref, 'r') as f:
  #      lines: list = f.readlines()
  #      import_reference: str = 'from ' + classes[c]['path_in_code'] + ' import ' + classes[c]['name']
  #      for line in lines:
  #        if line.startswith(import_reference) and classes[c]['name_obf'] is not None:
  #          updated_lines.append('from ' + classes[c]['path_in_code'] + ' import ' + classes[c]['name_obf'] + '\n')
  #        else:
  #          updated_lines.append(line)
  #    
  #    with open(ref, 'w') as f:
  #      f.writelines(updated_lines)
    
  #print(classes)

  # Compile into binary.
  # --follow-imports // Compiles the imports
  # --standalone // Compiles everything into one file.
  # --generate-c-only // Compiles to C only, no executable.
  # --verbose // Provides additional information.
  # --windows-disable-console // Disables CMD window on Windows.
  #os.system('nuitka3 --show-progress --python-flag="no_warnings" --standalone --recurse-all ' + build_path + '/main.py')

  # Move build files to build folder.
  #os.system('mv main.build ' + build_path + '/main.build')
  #os.system('mv main.dist ' + build_path + '/main.dist')
  #os.system('mv main.bin ' + build_path + '/main.bin')
