from pyscript import document


grade_7 = {"Ashlyn Tambilawan", "Jayleen Galang", "Kim Poleen", "Kevin De Chavez"}
grade_8 = {"Rhon Santos", "Joshua Evan", "Marisol Panopi"}
grade_9 = {"Dabe Adante", "Geoffrey Eman", "Jeanzel Enriqui"}
grade_10 = {"MJ Nuestro", "Prince Ulayao", "Franz Ulayao"}
members = grade_7.union(grade_8, grade_9, grade_10)


def render_members():
   output = document.getElementById("output1")
   output.textContent = "\n".join(sorted(members))
   document.getElementById("member_count").textContent = str(len(members))


def add_member(_event):
   first_name = document.getElementById("first_name").value.strip()
   last_name = document.getElementById("last_name").value.strip()
   output = document.getElementById("output1")

   if not first_name or not last_name:
      output.textContent = "Please enter both a first name and a last name."
      return

   full_name = f"{first_name} {last_name}".title()
   members.add(full_name)
   render_members()


render_members()



