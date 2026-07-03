// Add this new function at the end of the file
function copyToClipboard(elementId, button) {
  // Get the text from the parent element's content
  const textToCopy = document
    .getElementById(elementId)
    .textContent.split(":")
    .pop()
    .trim();
  navigator.clipboard
    .writeText(textToCopy)
    .then(() => {
    
      const originalText = button.innerHTML;
      button.innerHTML = "Copied!";
      setTimeout(() => {
        button.innerHTML = originalText;
      }, 1500); 
    })
    .catch((err) => {
      console.error("Failed to copy text: ", err);
    });
}
