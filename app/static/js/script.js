document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('prediction-form');
    const submitBtn = document.getElementById('submit-btn');
    const btnText = submitBtn.querySelector('.btn-text');
    const loader = submitBtn.querySelector('.loader');
    const resultContainer = document.getElementById('result-container');
    const resultCard = resultContainer.querySelector('.result-card');
    const resultIcon = document.getElementById('result-icon');
    const predictionResult = document.getElementById('prediction-result');
    const urlDisplay = document.getElementById('url-display');
    const modelDisplay = document.getElementById('model-display');
    const modelSelect = document.getElementById('model-select');
    const accuracyValue = document.getElementById('accuracy-value');

    // Update accuracy display
    function updateAccuracy() {
        const selectedOption = modelSelect.options[modelSelect.selectedIndex];
        const accuracy = selectedOption.getAttribute('data-accuracy');
        accuracyValue.textContent = accuracy || 'N/A';
    }

    modelSelect.addEventListener('change', updateAccuracy);
    updateAccuracy(); // Initial call

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const formData = new FormData(form);
        const data = {
            url: formData.get('url'),
            model: formData.get('model')
        };

        // UI Loading State
        setLoading(true);
        resultContainer.classList.add('hidden');

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();

            if (response.ok) {
                displayResult(result);
            } else {
                alert('Error: ' + (result.error || 'Something went wrong'));
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Failed to connect to the server.');
        } finally {
            setLoading(false);
        }
    });

    function setLoading(isLoading) {
        submitBtn.disabled = isLoading;
        if (isLoading) {
            btnText.classList.add('hidden');
            loader.classList.remove('hidden');
        } else {
            btnText.classList.remove('hidden');
            loader.classList.add('hidden');
        }
    }

    function displayResult(data) {
        const prediction = data.prediction;

        // Reset classes
        resultCard.className = 'result-card';
        resultIcon.className = 'fa-solid';

        if (prediction === 'benign') {
            resultCard.classList.add('result-safe');
            resultIcon.classList.add('fa-check');
            predictionResult.textContent = 'Safe URL';
        } else {
            // Treat all others as malicious/suspicious for now, or differentiate
            resultCard.classList.add('result-malicious');
            resultIcon.classList.add('fa-triangle-exclamation');
            predictionResult.textContent = `${prediction} Detected`;
        }

        urlDisplay.textContent = data.url;
        modelDisplay.textContent = `Analyzed by ${data.model}`;

        resultContainer.classList.remove('hidden');
    }
});
