function calculateDerivative() {
    const functionInput = document.getElementById('functionInput').value;
    try {
        const expr = math.parse(functionInput);
        const derivative = math.derivative(expr, 'x');
        const derivativeStr = derivative.toString();

        document.getElementById('derivativeOutput').innerText = derivativeStr;

        plotFunctionAndDerivative(functionInput, derivativeStr);
    } catch (error) {
        alert('Error al calcular la derivada. Verifique la entrada.');
    }
}

function clearInputs() {
    document.getElementById('functionInput').value = '';
    document.getElementById('derivativeOutput').innerText = '';
    Plotly.purge('plot');
}

function plotFunctionAndDerivative(func, derivative) {
    const xValues = math.range(-10, 10, 0.1).toArray();
    const funcValues = xValues.map(x => math.evaluate(func, { x }));
    const derivativeValues = xValues.map(x => math.evaluate(derivative, { x }));

    const funcTrace = {
        x: xValues,
        y: funcValues,
        mode: 'lines',
        name: 'f(x)'
    };

    const derivativeTrace = {
        x: xValues,
        y: derivativeValues,
        mode: 'lines',
        name: "f'(x)"
    };

    const layout = {
        title: 'Función y su Derivada',
        xaxis: { title: 'x' },
        yaxis: { title: 'y' }
    };

    Plotly.newPlot('plot', [funcTrace, derivativeTrace], layout);
}
