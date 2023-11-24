lang=input("Input the language : ")
name=input("Input the name of the person : ")
def hi(lang, name):
    if lang == "ru":
        print (f"Привет {name}!")
    elif lang=="en":
        print (f"hello {name}!")
    elif lang=="ro":
         print (f"Salut {name}!")

hi (lang, name)

