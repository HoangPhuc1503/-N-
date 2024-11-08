document.addEventListener("DOMContentLoaded", function() {
    // const hoTen = document.getElementById('user-name').textContent;
    var idcanbo = parseInt(document.querySelector(".id-canbo").textContent);
    let tenDN = localStorage.getItem("tenDN");
    let mK = localStorage.getItem("mK");
    
    if (tenDN !== "" && mK !== "") {
        const formData = new FormData();
        formData.append('tenDN', tenDN);
        formData.append('mK', mK);
        fetch(`/checklogin?tenDN=${tenDN}&mK=${mK}`, {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success && data.user_info) {
                if(idcanbo !== data.user_info.idCanBo){
                    window.location.href = "/login";
                }
                else{
                    document.getElementById('auth-link').addEventListener('click', function(event) {
                        event.preventDefault(); 
                        
                        tenDN = localStorage.removeItem("tenDN");
                        mK = localStorage.removeItem("mK");
                        // hoTen.textContent = "";
                        window.location.href = "/login";
                    });
                }
            } else {
                window.location.href = "/login";
            }
        })
        .catch(error => {
            console.error('Lỗi khi gửi yêu cầu đăng nhập:', error);
        });
    } else {
        window.location.href = "/login";
    }
    
});


