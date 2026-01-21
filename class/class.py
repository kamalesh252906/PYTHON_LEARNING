#  class MovieTicket:
#     def __init__(self):
#         self.movie_details = []

#     def add_movie_details(self, title, price, total_tickets_available):
#         details = {
#             "title": title,
#             "price": price,
#             "total_tickets_available": total_tickets_available
#         }
#         self.movie_details.append(details)

#     def book_tickets(self, title, count):
#         for movie in self.movie_details:
#             if movie["title"] == title:
#                 if movie["total_tickets_available"] >= count:
#                     movie["total_tickets_available"] -= count
#                     print(f"{count} tickets booked successfully for {title}")
#                 else:
#                     print("Not enough tickets available")
#                 return
#         print("Movie not found")

#     def cancel_tickets(self, title, cancel):
#         for movie in self.movie_details:
#             if movie["title"] == title:
#                 movie["total_tickets_available"] += cancel
#                 print(f"{cancel} tickets cancelled successfully for {title}")
#                 return
#         print("Movie not found")

#     def check_availability(self, title):
#         for movie in self.movie_details:
#             if movie["title"] == title:
#                 print(f"Available tickets for {title}: {movie['total_tickets_available']}")
#                 return
#         print("Movie not found")


# # Example usage
# b = MovieTicket()
# b.add_movie_details("Ghilli", 99, 101)
# b.add_movie_details("Leo",190,20)
# b.book_tickets("Leo", 10)
# b.cancel_tickets("Leo", 5)
# b.check_availability("Leo")


# class ToDoList:
#     def __init__(self):
#         self.tasks = []
    # def add_task(self , task_id, task_name, status):
#         details = {"task_id" : task_id,"task_name" : task_name,"status" : status}
#         self.tasks.append(details)
#     def view_tasks(self):
#         print(self.tasks)
#     def delete_task(self , task_id: int):
#         for el in self.tasks:
#             if el["task_id"] == task_id:
#                 self.tasks.remove(el)
#                 print('deleted')
#                 break
#         else:
#             print('No task found')
#     def mark_completed(self,task_id):
#         for el in self.tasks:
#             if el["task_id"] == task_id:
#                 el["status"] = "completed"
#                 break
#         else:
#             print("Not found")
#     def filter_completed(self):
#         for el in self.tasks:
#             if el["status"] == "completed":
#                 print(el)
#     def clear_all(self):
#         del self.tasks
# a = ToDoList()
# a.add_task(1,'python','pending')
# a.add_task(2,'java','completed')
# a.add_task(3,'C-programming','pending')
# a.mark_completed(1)
# a.filter_completed()
# a.view_tasks()
# a.clear_all()
# a.view_tasks()



# class AppointmentList:
#     def __init__(self):
#         self.appointments = []
        
# class AppointmentBooking(AppointmentList):
#     def __init__(self):
#         super().__init__()

#     def book_appointment(self,id,patient, doctor, time):
#         details = {"id": id, "patient": patient, "doctor": doctor, "time": time}
#         self.appointments.append(details)
#     def cancel_appointments(self,id):
#         for el in self.appointments:
#             if el["id"] == id:
#                 self.appointments.remove(el)
#     def reschedule_appointment(self,id,time):
#         for el in self.appointments:
#             if el["id"] == id:
#                 el["time"] = time
#     def view_all_appointments(self):
#         print(self.appointments)


# saran = AppointmentBooking()
# saran.book_appointment(1,"jeeva","kalai","4:00AM")
# saran.book_appointment(2,"kamal","hari","12:00PM")
# # saran.cancel_appointments(1)
# saran.reschedule_appointment(2,"11:00PM")
# saran.view_all_appointments()



# class ContactBook:
#     def __init__(self):
#         self.contacts = []
#     def add_contact(self,name: str,phone_number: tuple,email: tuple):
#         details = {
#             "name":name,
#             "phone_number":phone_number,
#             "email":email
#         }
#         self.contacts.append(details)
#     def get_phone(self,name):
#         for el in self.contacts:
#             if el["name"] == name:
#                 print(el["phone_number"])
#     def update_phone(self,name,phone_number):
#         for el in self.contacts:
#             if el["name"] == name:
#                 el["phone_number"] = phone_number
#     def delete_phone(self,name):
#         for el in self.:
#             if el["name"] == name:
#                 self.contacts.remove(el)
#     def view_lists(self):
#         print(self.contacts)
# book = ContactBook()
# book.add_contact("hari", ("9994254379"), ("alice@email.com"))
# book.add_contact("John", ("9994254379"), ("alice@email.com"))
# book.get_phone("hari")
# book.update_phone("hari",("9677085823"))
# book.delete_phone("hari")
# book.view_lists()









        