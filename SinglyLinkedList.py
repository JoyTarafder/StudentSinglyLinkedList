class Node:
  def __init__(self, data):
    self.data = data 
    self.next = None

class SinglyLinkedList: # Linked LList
  def __init__(self):
    self.head = None 
    self.size = 0

  def insert_student(self, new_name, new_cgpa): # Append Student Data (Name, CGPA)
    new_node = Node((new_name,new_cgpa)) # Use Tuple
    if self.head is None: # List is empty
      self.head = new_node 
    else:
      current_node = self.head # Current Node Access 1st data
      while current_node.next: # Current Node next data is not None (Loop)
        current_node = current_node.next # Access next data
      current_node.next = new_node # Store new data
    self.size += 1 # List Size Update

  def show_last_student(self): # Show Last Student Name and CGPA
    if self.size == 0:
      print("List is empty")
    else:
      current_node = self.head  # Current Node Access 1st data
      while current_node.next is not None:
          if current_node.next.next == None:
            current_node = current_node.next # Access next data
            print("Last Student:",current_node.data)
            return
          current_node = current_node.next # Access next data

  def sort_student(self): # Sorting All Student Name
    if self.size == 0:
      print("List is empty")
    else:
      current_node = self.head  # Current Node Access 1st data
      name_list = [] # Empty List
      while current_node is not None:
        name_list.append(current_node.data[0]) # Access Student Name Data and Append List
        current_node = current_node.next # Access next data
      name_list.sort()
      print(f"Sorting All Student Name List: {','.join(name_list)}") # Print Sorting All Student Name List
      # print(f"Sorting All Student Name List: {sorted(name_list)}") # Print Sorting All Student Name List

  def calculate_avg_CGPA(self): # calculating average CGPA
    if self.size!=0:
      sum = 0
      count = 0
      current_node = self.head  # Current Node Access 1st data
      while current_node is not None:
        count +=1 # calculate how many student data
        sum+= current_node.data[1] # Access student cgpa and use sum function
        current_node = current_node.next # Access next data 
    print("Calculate Average CGPA : %.3f " % (sum/count))

  def print_all(self): # Print all student data
    counter = 0
    current_node = self.head  # Current Node Access 1st data
    while current_node is not None:
      counter +=1 # calculate how many student data
      print(f"Student {counter}. {current_node.data}") # Print Student Data
      current_node = current_node.next # Access next data

s = SinglyLinkedList()
s.insert_student( 'Rahim',3.5)
s.insert_student('Karim',3.75)
s.insert_student('Jamal',3.2)
s.insert_student('Nafis',3.85)

s.print_all()
s.sort_student()
s.show_last_student()
s.calculate_avg_CGPA()