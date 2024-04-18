# -*- coding: utf-8 -*-
"""R_Project_1.R

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YmWtlAhrip_eam6HjGsZPZ585QTaQjV7

SAMPLE QUESTIONS
"""

# 1.	Create a vector called stock.prices with the following data points: 23,27,23,21,34.

# Stock prices
stock.prices = c(23, 27, 23, 21, 34)
stock.prices

# Logical vector for even numbers
even.numbers = numbers %% 2 == 0  # Modulo operator for even check

# 2.	Create a numeric vector containing the numbers 1 to 10.

# Numbers 1 to 10
numbers = 1:10
numbers

# 3.	Calculate the sum of these numbers.
sum(numbers)

# 4.	Create a logical vector indicating which numbers are even.
# Logical vector for even numbers
even.numbers = numbers %% 2 == 0  # Modulo operator for even check
even.numbers

# 5.	Use the plot() function to create a scatter plot of the mtcars dataset, plotting mpg (miles per gallon) against hp (horsepower).
library(ggplot2)  # Using ggplot2 for better customization

ggplot(mtcars, aes(x = hp, y = mpg)) +
  geom_point() +
  labs(title = "MPG vs. Horsepower", x = "Horsepower", y = "Miles per Gallon")

# 6.	Given a vector a = c("a", "b", "c", "d", "e"), extract the 2nd and 4th elements.
a = c("a", "b", "c", "d", "e")
second_and_fourth = a[c(2, 4)]  # Output: c("b", "d")
second_and_fourth

# 7.	From the mtcars dataset, select the rows where cyl (cylinders) is 4 and only the columns mpg, hp, and wt.
mtcars_sub = mtcars[mtcars$cyl == 4, c("mpg", "hp", "wt")]
mtcars_sub

# 8.	Create a list my_list that contains three elements: a numeric vector (1, 2, 3), a character vector (“a”, “b”, “c”), and a matrix with 2 rows and 2 columns.
my_list = list(
  numbers = 1:3,
  letters = c("a", "b", "c"),
  matrix = matrix(1:4, nrow = 2)
)
my_list

# 9.	Add a new element to my_list that is a logical vector (TRUE, FALSE).
my_list[[length(my_list) + 1]] = c(TRUE, FALSE)
my_list

# 10.	Create character vector words with the elements “R”, “is”, “fun”.

words = c("R", "is", "fun")
words

# 11.	Use a function to concatenate these words into a single string: “R is fun”.
sentence = paste(words, collapse = " ")
sentence

# 12.	Replace “fun” with “awesome” in the concatenated string.
new_sentence = gsub("fun", "awesome", sentence)
new_sentence

# 13.	From a numeric vector to a character vector: v_num = c(1, 2, 3)
v_num=c(1,2,3)
char=as.character(v_num)
char
typeof(char)

# 14.	From a character vector to a factor: v_char = c("low", "medium", "high")
v_char = c("low", "medium", "high")
fact=factor(v_char)
fact
typeof(fact)

# 15.	From a factor to a numeric vector, considering the factor levels as numeric values:
f = factor(c(1, 2, 3))
numer=as.numeric(f)
numer
typeof(numer)

# 16.	colors = c(“red”, “blue”, “green”, “blue”, “red”, “green”, “green”, “red”)
# 1.	Convert colors into a factor, f_colors.
# 2.	Print the levels of f_colors.
# 3.	How would you reorder the levels of f_colors so that “green” comes first?

colors = c("red", "blue", "green", "blue", "red", "green", "green", "red")
f_colors = factor(colors)

# Levels
levels(f_colors)

# Reordering levels
f_colors = factor(colors, levels = c("green", "red", "blue"))
levels(f_colors)

# 17.	my_list = list(name = “Alice”, age = 30, hobbies = c(“Cycling”, “Art”, “Music”)) my_df = data.frame(Name = c(“Alice”, “Bob”), Age = c(25, 30))
# 1.	Access and print the hobbies element from my_list.
# 2.	Add a new column Occupation to my_df with values “Doctor” for Alice and “Engineer” for Bob.

my_list = list(name = 'Alice', age = 30, hobbies = c('Cycling', 'Art', 'Music'))
my_df = data.frame(Name = c('Alice', 'Bob'), Age = c(25, 30))

# Access hobbies
cat("Hobbies:", my_list$hobbies, "\n")

# Add Occupation column
my_df$Occupation = c("Doctor", "Engineer")
my_df$Occupation
my_df

"""DATA FRAMES QUESTIONS"""



# QUESTION 1:

# 1.	Create a data frame named df_students with the following columns: ID, Name, Age, and Grade. Populate it with data for 5 students. Perform the following operations:
# 1.	Add a new column Passed that indicates with TRUE or FALSE whether each student passed (assume a passing grade is at least 60).
# 2.	Select and print only the rows of students who are 18 years or older.

# Sample student data
students = data.frame(
  ID = c(1001, 1002, 1003, 1004, 1005),
  Name = c("RAJA", "SACHIN", "ROJA", "RAHUL", "JHONY"),
  Age = c(19, 18, 20, 17, 22),
  Grade = c(85, 72, 90, 55, 68)
)

# Create data frame
df_students = students
df_students

# Add Passed column
df_students$Passed = df_students$Grade >= 60
df_students$Passed

# Select students 18 or older (consider row names for clarity)
print(df_students[df_students$Age >= 18, ])

QUESTION 2:

# 2.	Suppose you have two data frames, df_A and df_B. df_A contains student IDs and names, while df_B contains student IDs and their corresponding courses.
#  Write R code to merge these data frames so each row contains a student’s ID, name, and course.

df_A = data.frame(
    student_IDs = c(1001, 1002, 1003, 1004, 1005),
    Name = c("RAJA", "SACHIN", "ROJA", "RAHUL", "JHONY")
)
df_A

df_B = data.frame(
    student_IDs = c(1001, 1002, 1003, 1004, 1005),
    courses = c("EEE", "ECE", "MECH", "CSE", "IT")
)
df_B

merged_df = merge(df_A, df_B, by = "student_IDs", all.x = TRUE)  # all.x = TRUE keeps all rows from df_A
merged_df

# QUESTION 3:

install.packages('dplyr')

library(dplyr)

# 3.	Given a data frame df_sales with columns Date, ProductID, Quantity, and Price, write R code to calculate the total sales (Quantity * Price) for each product.
# 1.	Note: Generate your own data set.

# Sample sales data
df_sales = data.frame(
  Date = as.Date(c("2024-04-01", "2024-04-01", "2024-04-02", "2024-04-02")),
  ProductID = c(101, 102, 101, 103),
  Quantity = c(2, 1, 3, 4),
  Price = c(10, 15, 10, 5)
)

# Total sales per product
total_sales = df_sales %>%
  group_by(ProductID) %>%
  summarize(TotalSales = sum(Quantity * Price))

print(total_sales)

# QUESTION 4:

# 4.	For iris data set.
# 1.	Calculate the average Sepal.Length for each Species.
# 2.	Create a new column Sepal.Area which is the product of Sepal.Length and Sepal.Width.
# 3.	Find the species with the highest average Sepal.Area.

# Load the iris dataset
data(iris)

# Average Sepal Length per Species
avg_sepal_length = iris %>%
  group_by(Species) %>%
  summarize(AvgLength = mean(Sepal.Length))

print(avg_sepal_length)

# Sepal Area and Species with highest average
iris$Sepal.Area = iris$Sepal.Length * iris$Sepal.Width
iris$Sepal.Area

highest_area_species = iris %>%
  group_by(Species) %>%
  summarize(AvgArea = mean(Sepal.Area)) %>%
  arrange(desc(AvgArea)) %>%
  head(1)  # Get the first row (species with highest average)

print(highest_area_species)

QUESTION 5:

# 5.	For airquality data set.
# 1.	Calculate the average Ozone level for each month, excluding missing values.
# 2.	Determine the month with the highest average Ozone level.
# 3.	Create a new data frame with Month and Temp columns, excluding days with missing Ozone values.

library(airquality)  # Load airquality data set

data(airquality)

# Average Ozone per month (excluding missing values)
avg_ozone_month = airquality %>%
  filter(!is.na(Ozone)) %>%  # Filter out missing Ozone values
  group_by(Month) %>%
  summarize(AvgOzone = mean(Ozone))

print(avg_ozone_month)

# Month with highest average Ozone
highest_ozone_month <- avg_ozone_month %>%
  arrange(desc(AvgOzone)) %>%
  head(1)  # Get the first row (month with highest average)

print(highest_ozone_month)

# Filter days with missing Ozone and create new data frame
filtered_airquality <- airquality[complete.cases(airquality[, "Ozone"]), ]
new_df <- filtered_airquality[, c("Month", "Temp")]

print(new_df)





"""**DPLYR QUESTIONS**"""

# 1.	Return rows of cars that have an mpg value greater than 20 and 6 cylinders.
library(dplyr)
data(mtcars)

# Filter and select cars with mpg > 20 and cyl = 6
filtered_mtcars = mtcars %>%
  filter(mpg > 20, cyl == 6) %>%
  select(mpg, hp)  # Select mpg and hp columns
print(filtered_mtcars)

# 2.	Reorder the Data Frame by cyl first, then by descending wt.
# Reorder by cyl and wt (descending)
reordered_mtcars = mtcars %>%
  arrange(cyl, desc(wt))  # Arrange by cyl ascending, wt descending
print(reordered_mtcars)

# 3.	Select only the columns mpg and hp.
# Select only mpg and hp columns
selected_mtcars = mtcars[, c("mpg", "hp")]

# Print the selected data
print(selected_mtcars)

# 4.	Select the distinct values of the gear column.
# Distinct values of gear
distinct_gears = mtcars %>%
  distinct(gear)  # Get unique gear values
print(distinct_gears)

# 5.	Create a new column called “Performance” which is calculated by hp divided by wt.
# Create Performance column (hp / wt)
mtcars_performance = mtcars %>%
  mutate(Performance = hp / wt)  # Add new column with hp / wt calculation
print(mtcars_performance)

# 6.	Find the mean mpg value using dplyr.
# Mean mpg using dplyr
mean_mpg = mtcars %>%
  summarize(AvgMPG = mean(mpg))  # Calculate average mpg
print(mean_mpg)

# 7.	Use pipe operators to get the mean hp value for cars with 6 cylinders.
# Mean hp for 6 cylinders with pipe operator
mean_hp_cyl6 = mtcars %>%
  filter(cyl == 6) %>%  # Filter cars with 6 cylinders
  summarize(AvgHP = mean(hp))  # Calculate average hp
print(mean_hp_cyl6)



"""**FUNCTION QUESTIONS**"""

# 1.	Create a function that takes in a name as a string argument, and prints out “Hello name”.
greet = function(name) {
  cat("Hello", name, "\n")
}

greet("RAJA")

# 2.	Create a function that takes in a name as a string argument and returns a string of the form - “Hello name”.
greet_and_return = function(name) {
  return(paste("Hello", name))
}

greeting = greet_and_return("RAJA")
print(greeting)

# 3.	Create a function that will return the product of two integers.
multiply = function(x, y) {
  return(x * y)
}

product = multiply(5, 3)
print(product)

# 4.	Create a function to check the count of numbers
# 1.	Ex. x = c(1,1,1,2,2,2,3,12,3,4,5,3) output should be how many times each element is present in the vector.
count_occurrences = function(x) {

  return(table(x))
}

x = c(1, 1, 1, 2, 2, 2, 3, 12, 3, 4, 5, 3)
counts = count_occurrences(x)
print(counts)

# 5.	Create a function categorize_age that takes an age (numeric value) as input and
#  returns “Child” if the age is less than 18, “Adult” if the age is between 18 and 64, inclusive, and “Senior” if the age is 65 or above.

categorize_age = function(age) {
  if (age < 18) {
    return("Child")
  } else if (age <= 64) {
    return("Adult")
  } else {
    return("Senior")
  }
}

age_category = categorize_age(25)
print(age_category)

# 6.	Write a function average_salary_by_age_group that takes a data frame with columns Age and
# Salary and returns a new data frame with two columns, AgeGroup and AverageSalary, where AgeGroup is “Young” (ages below 30), “Middle” (ages 30 to 50),
#  and “Senior” (ages above 50), and AverageSalary is the average salary for each age group.



average_salary_by_age_group = function(data) {
  data = mutate(data, AgeGroup = case_when(
    Age < 30 ~ "Young",
    Age >= 30 & Age <= 50 ~ "Middle",
    Age > 50 ~ "Senior"
  ))

  result = data %>%
    group_by(AgeGroup) %>%
    summarise(AverageSalary = mean(Salary))

  return(result)
}
# Sample data frame
data = data.frame(Age = c(25, 35, 45, 55, 28, 42, 50),
                   Salary = c(50000, 60000, 70000, 80000, 55000, 65000, 75000))

# Call the function
result = average_salary_by_age_group(data)
print(result)

# 7.	Given a data frame df with columns Length and Width representing dimensions of rectangles,
# write a function area_rectangle that calculates the area of each rectangle.
# Then, use apply(), lapply(), or sapply() to apply this function to df to add a new column Area to the data frame.

# Define the function to calculate area of rectangle
area_rectangle = function(length, width) {
  area = length * width
  return(area)
}

# Sample data frame
df = data.frame(Length = c(5, 6, 7),
                 Width = c(2, 3, 4))

# Apply the function using sapply and add a new column 'Area'
df$Area = sapply(df$Length, function(x) area_rectangle(x, df$Width))

# Print the updated data frame
print(df)



"""**GGPLOT QUESTIONS**"""

install.packages('ggplot2')

install.packages('ggthemes')

install.packages('cowplot')

install.packages('gganimate')



# Load required packages
library(ggplot2)

data(mtcars)

# Task 1: Histogram of hwy mpg values from mtcars dataset
histogram = ggplot(mtcars, aes(x = mpg)) +  # 'mpg' should be used instead of 'hwy'
  geom_histogram(binwidth = 2, fill = "skyblue", color = "black") +
  labs(title = "Histogram of Highway MPG Values", x = "Highway MPG", y = "Frequency")
print(histogram)

data(mtcars)
x=mtcars

# Task 2: Barplot of car counts per manufacturer with color fill defined by cyl count
barplot = ggplot(mtcars, aes(x = factor(am), fill = factor(cyl))) +
  geom_bar() +
  labs(title = "Car Counts per Manufacturer by Cylinder Count", x = "Manufacturer", y = "Car Count") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
print(barplot)





# Task 3: Scatterplot of volume versus sales using txhousing dataset
data(txhousing)
scatterplot = ggplot(txhousing, aes(x = sales, y = volume)) +
  geom_point(alpha = 0.7, color = "blue") +
  labs(title = "Scatterplot of Volume versus Sales", x = "Sales", y = "Volume")
print(scatterplot)

# Task 4: Scatterplot with adjusted alpha and color for better clarity
scatterplot_adjusted = ggplot(txhousing, aes(x = sales, y = volume)) +
  geom_point(alpha = 0.5, color = "green") +
  labs(title = "Scatterplot of Volume versus Sales (Adjusted)", x = "Sales", y = "Volume")
print(scatterplot_adjusted)

# Task 5: Scatterplot with a smooth fit line
scatterplot_smooth = ggplot(txhousing, aes(x = sales, y = volume)) +
  geom_point(alpha = 0.5, color = "red") +
  geom_smooth(method = "lm", se = FALSE) +  # Add linear model fit line without confidence intervals
  labs(title = "Scatterplot of Volume versus Sales with Smooth Fit Line", x = "Sales", y = "Volume")
print(scatterplot_smooth)



"""**AIR QUALITY DEFAULT DATA**"""



# Load required packages
library(ggplot2)

# Create the scatterplot with ggplot2 using airquality dataset
scatterplot = ggplot(airquality, aes(x = Day, y = Ozone, color = factor(Month))) +
  geom_point() +  # Scatterplot
  geom_smooth(method = "lm", se = FALSE) +  # Add a smooth trend line
  labs(title = "Ozone Levels by Day of the Month", x = "Day of the Month", y = "Ozone Levels") +
  scale_color_discrete(name = "Month")  # Set legend title

# Print the plot
print(scatterplot)

use check weight default data

# Load required packages
library(ggplot2)

data(ChickWeight)

# Plot Time on the x-axis and weight on the y-axis
plot = ggplot(ChickWeight, aes(x = Time, y = weight, color = factor(Diet), group = Chick)) +
  geom_line() +
  labs(title = "Weight over Time by Diet", x = "Time", y = "Weight") +
  scale_color_discrete(name = "Diet") +
  theme_minimal()
print(plot)



USE diamonds default data
Create a histogram to show the distribution of carat sizes. Then, refine your plot by:
1.	Filling the bars based on the cut quality of the diamonds.
2.	Limiting the x-axis to diamonds up to 3 carats for better detail.



# Create a histogram of carat sizes
histogram = ggplot(diamonds, aes(x = carat)) +
  geom_histogram(binwidth = 0.5, fill = "skyblue", color = "black") +
  labs(title = "Distribution of Carat Sizes", x = "Carat", y = "Frequency")

# Refine the plot by filling bars based on the cut quality and limiting x-axis to diamonds up to 3 carats
refined_plot = histogram +
  geom_histogram(data = subset(diamonds, carat <= 3), aes(fill = cut), alpha = 0.7) +
  scale_fill_manual(values = c("Fair" = "red", "Good" = "orange", "Very Good" = "yellow", "Premium" = "green", "Ideal" = "blue")) +
  xlim(0, 3)

# Print the refined plot
print(refined_plot)



"""**MATRIX QUESTIONS**"""



# Define matrices B, C, and A
B = matrix(c(1, 2, 3, 4), nrow = 2)
C = matrix(c(2, 0, 1, 2), nrow = 2)
A = matrix(1:9, nrow = 3)

# 1. Sum of B and C
sum_B_C = B + C
print("1. Sum of B and C:")
print(sum_B_C)

# 2. Product of B and C (matrix multiplication)
product_B_C = B %*% C
print("2. Product of B and C (matrix multiplication):")
print(product_B_C)

# 3. Sum of each row in A
sum_each_row_A = rowSums(A)
print("3. Sum of each row in A:")
print(sum_each_row_A)

# 4. Mean value of each column in A
mean_each_column_A = colMeans(A)
print("4. Mean value of each column in A:")
print(mean_each_column_A)

# 5. Set all the elements to 0 if they are divisible by 2
A[A %% 2 == 0] <- 0
print("5. Matrix A with elements set to 0 if divisible by 2:")
print(A)





"""**STATEMENT QUESTIONS**"""

# 1.	Write a script that will
#  print “Even Number” if the variable x is an even number, otherwise print “Not Even”.

# Define the variable x
x = 10

# Check if x is an even number
if (x %% 2 == 0) {
  print("Even Number")
} else {
  print("Not Even")
}

# 2.	Write a script that will print ‘Is a Matrix’ if the variable x is a matrix, otherwise print “Not a Matrix”.
#  Hint: You may want to check out help(is.matrix)


# Define the variable x
x = matrix(1:9, nrow = 3)

# Check if x is a matrix
if (is.matrix(x)) {
  print("Is a Matrix")
} else {
  print("Not a Matrix")
}

# 3.	Create a script that given a numeric vector x x=c(3,7,1),
#  will print out the elements in order from high to low i.e (1,3,7).
# You must use if,else if, and else statements for your logic.


# Define the numeric vector x
x = c(3, 7, 1)

# Sort the elements of x in descending order
x_sorted = sort(x, decreasing = TRUE)

# Print the sorted elements
print(x_sorted)

# 4.	Write a script that uses if,else if, and else statements to print
#  the max element in a numeric vector with 3 elements.
# 1.	Ex. x = c(3,7,1) 7 should be the output

# Define the numeric vector x
x = c(3, 7, 1)

# Find the maximum element using if-else statements
if (x[1] > x[2] && x[1] > x[3]) {
  print(x[1])
} else if (x[2] > x[1] && x[2] > x[3]) {
  print(x[2])
} else {
  print(x[3])
}


