async function analyzeSentiment() {
    const text = document.getElementById('inputText').value;
    const response = await fetch('/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text })
    });
    const result = await response.json();
    document.getElementById('result').innerText = `Sentiment: ${result.sentiment}`;
}
