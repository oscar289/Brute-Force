# Brute Force

Brute force is a method of solving a problem by trying every possible solution until the correct one is found. It is a simple and straightforward approach, but it may not always be the most efficient way to solve a problem.

Complexity is a measure of how difficult it is to solve a problem. Factors that can influence the complexity of a problem include the length of the target (e.g. a longer target may take longer to find), the character set (e.g. a larger character set may take longer to search through), and other factors such as the number of possible solutions.

Examples:

Target: "abc"

```
Length: 3
Character set: 26 lowercase letters
Average time to find: Very fast (less than a second)
```

Target: "abc123"

```
Length: 6
Character set: 26 lowercase letters + 10 digits
Average time to find: Fast (less than a minute)
```

Target: "abcdefghijklmnopqrstuvwxyz1234567890"

```
Length: 36
Character set: 26 lowercase letters + 10 digits
Average time to find: Relatively fast (less than an hour)
```

Target: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

```
Length: 62
Character set: 52 uppercase and lowercase letters + 10 digits
Average time to find: Moderate (a few hours)
```

Target: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"

```
Length: 94
Character set: 52 uppercase and lowercase letters + 10 digits + 32 special characters
Average time to find: Long (a few days)
```

Keep in mind that these are just rough estimates and the actual time required to find the target will depend on the specific hardware and software being used. Also, these estimates assume that the brute force algorithm is implemented optimally and that no other more efficient algorithms are available to solve the problem.

It is important to note that the complexity of a problem can have a significant impact on the time required to solve it using a brute force algorithm. As the length and character set of the target increase, the number of possibilities also increases, and it becomes much more time-consuming to search through them all. This is why it is important to consider the complexity of a problem when deciding whether to use a brute force approach and to choose an appropriate algorithm for the specific problem you are trying to solve.

Real life use cases:

Password cracking: Brute force is often used to crack passwords by trying every possible combination of characters until the correct password is found. This can be done manually, but it is more commonly done using automated tools that can try millions or billions of combinations per second.

Games: In some games, brute force can be used to try every possible move or strategy until the best one is found. This can be an effective approach in simple games, but it may not be practical for more complex games where there are many possible moves or strategies to consider.
