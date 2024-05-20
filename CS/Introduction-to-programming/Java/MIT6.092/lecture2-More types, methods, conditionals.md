# Lecture2-More types, methods, conditionals

- methods
- Conditionals 
- Variable Scope

# methods

Methods: Building Blocks

- Big programs are built out of small methods
- Methods can be individually developed, tested and reused
- User of method does not need to know how it works
- In Computer Science, this is called “abstraction”



```java
public static void main(String[] arguments)  
{
System.out.println(“hi”);
}
```

Parameters

```java
public static void NAME(TYPE NAME,TYPE NAME) {
STATEMENTS
}
To call:
NAME(EXPRESSION); 
```

Return Values

```java
public static TYPE NAME() {
STATEMENTS! return EXPRESSION; 
}
// void means “no type”
```

## Mathematical Functions

```java
Math.sin(x) 
Math.cos(Math.PI / 2) 
Math.pow(2, 3) 
Math.log(Math.log(x + y)) 
```

# Conditionals

## if statement

```java
if (CONDITION) {
	STATEMENTS
}
```

```java
if (CONDITION) {
	STATEMENTS
}else{
	STATEMENTS
}
```

```java
if (CONDITION) {
	STATEMENTS
}else if(CONDITION){
	STATEMENTS
}else if(CONDITION){
    STATEMENTS
}else{
    STATEMENTS
}
```

Comparison operators

- x > y: x is greater than y
- x < y: x is less than y
- x >= y: x is greater than or equal to x
- x <= y: x is less than or equal to y
- x == y: x equals y  (  equality: `==` , assignment: `=`  )
- `!`  flips true/false
- ``&&`` : logical AND
- `||` : logical OR

```java
public static void test(int x) {
    if (x > 5) {
        System.out.println(x + " is > 5");
    }
}
public static void main(String[] arguments) {
    test(6);
	test(5);
	test(4);
}
```

# Variable Scope

- Variables live in the block `({})` where they are defined (scope)
- Method parameters are like defining a new variable in the method



# Assignment: FooCorporation

- Method to print pay based on base pay and hours worked
- Overtime: More than 40 hours, paid 1.5 times base pay
- Minimum Wage: $8.00/hour
- Maximum Work: 60 hours a week



















