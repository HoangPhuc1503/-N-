   document.getElementById('title_content_bottom_left').addEventListener('click', function() {
    var contentDiv1 = document.getElementById('right-main-content_1');
    var contentDiv2 = document.getElementById('right-main-content_2');
    var button1 = document.getElementById('title_content_bottom_left');
    var button2 = document.getElementById('title_content_bottom_right');
            if (contentDiv1.style.display === 'none' || contentDiv1.style.display === '') {
                contentDiv1.style.display = 'block';
                contentDiv2.style.display = 'none';}
                button1.style.backgroundColor = '#1a9fa3';
                button2.style.backgroundColor = '#4E78BB';
      });

   document.getElementById('title_content_bottom_right').addEventListener('click', function() {
    var contentDiv1 = document.getElementById('right-main-content_1');
    var contentDiv2 = document.getElementById('right-main-content_2');
    var button1 = document.getElementById('title_content_bottom_left');
    var button2 = document.getElementById('title_content_bottom_right');
            if (contentDiv2.style.display === 'none' || contentDiv2.style.display === '') {
                contentDiv2.style.display = 'block';
                contentDiv1.style.display = 'none';}
                button1.style.backgroundColor = '#4E78BB';
                button2.style.backgroundColor = '#1a9fa3';
      });


