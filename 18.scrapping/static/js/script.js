document.addEventListener('DOMContentLoaded', () => {
    const hoverDiv = document.getElementById('hoverDiv');
    
    hoverDiv.addEventListener('mouseenter', () => {
      hoverDiv.style.backgroundColor = '#ffcc00';
    });
    
    hoverDiv.addEventListener('mouseleave', () => {
      hoverDiv.style.backgroundColor = '#eee';
    });
  });