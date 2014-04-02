def reverse(str):
  if str == "":
    return ""
  # Return the reverse of the rest of the string
  # concatinated with the first element!
  return reverse(str[1::]) + str[0]

print reverse("colin")
