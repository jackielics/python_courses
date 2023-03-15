a_int = 1
print(f"set\t{id(a_int)}")
a_int = 2
print(f"int\t{id(a_int)}")

a_bool = True
print(f"bool\t{id(a_bool)}")
a_bool = False
print(f"bool\t{id(a_bool)}")

a_float = 1.1
print(f"float\t{id(a_float)}")
a_float = 1.2
print(f"float\t{id(a_float)}")

a_complex = complex(1,2)
print(f"complex\t{id(a_complex)}")
a_complex = complex(1,3)
print(f"complex\t{id(a_complex)}")

a_string = '12'
print(f"string\t{id(a_string)}")
a_string.replace('2', '3')
print(f"string\t{id(a_string)}")

a_tuple = (1,2)
print(f"tuple\t{id(a_tuple)}")
a_tuple = (1,3)
print(f"tuple\t{id(a_tuple)}")

