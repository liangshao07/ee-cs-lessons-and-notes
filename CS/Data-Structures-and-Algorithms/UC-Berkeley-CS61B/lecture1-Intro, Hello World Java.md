# lecture1-Intro, Hello World Java

- Introduction Course
- Hello World
- Static Typing
- Declaring Functions

## Introduction Course

### Prerequisites

Assumes solid foundation in programming fundamentals, including:

- Object oriented programming, recursion, lists, and trees.

### What is 61B about?

- Writing code that runs efficiently.
    - Good algorithms.
    - Good data structures.
- Writing code efficiently.
    - Designing, building, testing, and debugging large programs.
    - Use of programming tools.
        - git, IntelliJ, JUnit, and various command line tools.
    - Java (not the focus of the course!)

### TMWLO: A Small Minority

- Lectures: 
    - Introduction to new material.
- Reading: 
    - More thorough introduction.
- Discussion Section, Vitamins, and Study Guides: 
    - Practice with concepts and Java syntax.
- Labs, Weekly(ish) Homework, and Your Own Experimentation: 
    - Practice with tools, programming techniques, Java syntax, and algorithms and data structures.
- Projects: 
    - Similar to labs and HW, but larger and include a design component.

### Course Structure

Phase 1: Programming Intensive Introduction to Java. 

- Weeks 1-4.
- One browser-based programming HW (this HW0 is optional).
- Three labs to introduce you to various tools (starting this week).
- Two projects (proj0 and proj1).

Phase 2: Advanced Programming

- Weeks 5-7.
- One small HW (HW1).
- One large project, due ~3/5.
    - New: You design your own explorable world (within some constraints).
- Labs to support large project.

Phase 3: Data Structures and Algorithms

- Weeks 8-14
- Incredibly important and foundational material: Expect an CS job interview to lean heavily on this part of the course.
- Labs: Implement a data structure or algorithm.
    - Each lab ends with a TA led discussion of best implementation.
- Six HWs: Apply a data structure or algorithm toward a real world problem.
    - Two released during RRR week. Can be used to makeup missed homeworks earlier, or for practice.
- One very challenging data structure/algorithms project (but not as big as project 2).

## Hello World

**Our First Java Program.** Printing Hello World is as easy as:

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello world!");
    }
}
```

**Key Syntax Features.** Our first programs reveal several important syntax features of Java:

- All code lives inside a class.
- The code that is executed is inside a function, a.k.a. method, called `main`.
- Curly braces are used to denote the beginning and end of a section of code, e.g. a class or method declaration.
- Statements end with semi-colons.
- Variables have declared types, also called their “static type”.
- Variables must be declared before use.
- Functions must have a return type. If a function does not return anything, we use void,
- The compiler ensures type consistency. If types are inconsistent, the program will not compile.

### Running a Java Program

![compilationflow](./assets/compilation_figure.svg)

For example, to run `HelloWorld.java`, we'd type the command `javac HelloWorld.java` into the terminal, followed by the command `java HelloWorld`. The result would look something like this:

```bash
$ javac HelloWorld.java
$ java HelloWorld
Hello World! 
```

## Static Typing

**Static Typing.** Static typing is (in my opinion) one of the best features of Java. It gives us a number of important advantages over languages without static typing:

- Types are checked before the program is even run, allowing developers to catch type errors with ease.
- If you write a program and distribute the compiled version, it is (mostly) guaranteed to be free of any type errors. This makes your code more reliable.
- Every variable, parameter, and function has a declared type, making it easier for a programmer to understand and reason about code.

There are downside of static typing, to be discussed later.

## Variables and Loops

The program below will print out the integers from 0 through 9.

```java
public class HelloNumbers {
    public static void main(String[] args) {
        int x = 0;
        while (x < 10) {
            System.out.print(x + " ");
            x = x + 1;
        }
    }
}
```

- Our variable x must be declared before it is used, *and it must be given a type!*
- Our loop definition is contained inside of curly braces, and the boolean expression that is tested is contained inside of parentheses.
- Our print statement is just `System.out.print` instead of `System.out.println`. This means we should not include a newline (a return).
- Our print statement adds a number to a space. This makes sure the numbers don't run into each other. Try removing the space to see what happens.
- When we run it, our prompt ends up on the same line as the numbers (which you can fix in the following exercise if you'd like).

## Declaring Functions













