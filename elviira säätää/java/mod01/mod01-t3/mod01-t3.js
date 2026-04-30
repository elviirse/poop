// Write a program that prompts for three integers.
// The program prints the sum, product and average of the numbers to the HTML document. (3p)

// kokonaisluvut
    const num1 = parseInt(prompt("First integer: "))
    const num2 = parseInt(prompt("Second integer: "))
    const num3 = parseInt(prompt("Third integer: "))

// matikka

    const sum = num1 + num2 + num3;
    const product = num1 * num2 * num3;
    const average = sum / 3;

// näkyy käyttäjälle

    document.querySelector('#target').textContent =
        "Sum: " + sum +
        ", Product: " + product +
        ", Average: " + average;

