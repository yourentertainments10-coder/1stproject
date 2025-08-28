
// Show a loading spinner when the form is submitted
document.addEventListener('DOMContentLoaded', function() {
	var form = document.querySelector('form');
	if (form) {
		form.addEventListener('submit', function() {
			let loader = document.createElement('div');
			loader.id = 'loader';
			loader.style.position = 'fixed';
			loader.style.top = '0';
			loader.style.left = '0';
			loader.style.width = '100vw';
			loader.style.height = '100vh';
			loader.style.background = 'rgba(255,255,255,0.7)';
			loader.style.display = 'flex';
			loader.style.alignItems = 'center';
			loader.style.justifyContent = 'center';
			loader.style.zIndex = '9999';
			loader.innerHTML = '<div style="font-size:2em;">Loading...</div>';
			document.body.appendChild(loader);
		});
	}

	// Remove loader after page load
	window.addEventListener('pageshow', function() {
		var loader = document.getElementById('loader');
		if (loader) loader.remove();
	});

	// Smooth scroll to recommendations if present
	var rec = document.getElementById('recommendations');
	if (rec) {
		rec.scrollIntoView({ behavior: 'smooth' });
	}
});
