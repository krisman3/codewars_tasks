def student_scores(list_names, list_scores):
    student_dict = {}
    for name, score in zip(list_names, list_scores):
        student_dict[name] = score

    return student_dict


lst1 = ['Anton', 'Georgi', 'Ivan']
lst2 = [66, 23, 41]
print(student_scores(lst1, lst2))
