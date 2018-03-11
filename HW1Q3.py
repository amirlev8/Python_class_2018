# python_class_2018. HW1 Q3. Amir Levi 032551087.

art = [['Hadas', 'Nora', 'Shir', 'Lidor', 'Ortal'],
             ['Grade A', 30, 90, 78, 80], ['Grade B', 70, 95, 20, 80]]


phylosophy = [['Hadas', 'Nora', 'Shir', 'Lidor', 'Ortal'],
                   ['Grade A', 48, 18, 45, 100], ['Grade B', 50, 32, 45, 98]]



def compare_subjects_within_student(sun_class, phylosophy):
  """
  Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.
  Choice for the data structure of the function's arguments is up to you.
  """

  Highest_grade1 =[]
  Highest_grade1.append(art[0][1:])
  var = max(art[1][1:], art[2][1:])
  Highest_grade1.append(var)

#finding the max grade btween tow semesters for phylosophy
  Highest_grade2 = []
  Highest_grade2.append(phylosophy[0][1:])
  var = max(phylosophy[1][1:], phylosophy[2][1:])
  Highest_grade2.append(var)

  check_list = dict()
  for j in Highest_grade1[0]:
	  if j in Highest_grade2[0]:
		  i1 = Highest_grade1[0].index(j)
		  i2 = Highest_grade1[0].index(j)
		  if Highest_grade1[1][i1] > Highest_grade2[1][i2]:
			  check_list[j] = 'art'
		  else:
			  check_list[j] = 'phylosophy'
  return (check_list)

a=compare_subjects_within_student(art,phylosophy)
print(a)
