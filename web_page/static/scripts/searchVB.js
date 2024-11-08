
document.addEventListener("DOMContentLoaded", function() {
    const searchForm = document.getElementById("search-form");
    searchForm.addEventListener("submit", function(event) {
        event.preventDefault(); // Ngăn chặn việc gửi form đi
        const idCanBo = document.querySelector('.id-canbo').textContent;
    
        const formData = new FormData(searchForm);
        const searchTerm = formData.get("key");
    
        if (searchTerm.trim() !== "") {
            searchForm.action = `/hethong/vanbandi/search/${idCanBo}?key=${searchTerm}`; 
            searchForm.submit();
            
        }
        else{
            alert("Vui lòng nhập từ khóa tìm kiếm.");
        }
    });
});



// Văn bản đến

document.addEventListener("DOMContentLoaded", function() {
    const searchFormvbden = document.getElementById("search-form-VBden");
    searchFormvbden.addEventListener("submit", function(event) {
        event.preventDefault(); // Ngăn chặn việc gửi form đi
        const idCanBo = document.querySelector('.id-canbo').textContent;
    
        const formData = new FormData(searchFormvbden);
        const searchTerm = formData.get("key");
    
        if (searchTerm.trim() !== "") {
            searchFormvbden.action = `/hethong/vanbanden/search/${idCanBo}?key=${searchTerm}`; 
            searchFormvbden.submit();
            
        }
        else{
            alert("Vui lòng nhập từ khóa tìm kiếm.");
        }
    });
});
