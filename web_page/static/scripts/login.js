document.addEventListener("DOMContentLoaded", function() {
    const loginForm = document.getElementById("form-login");
    loginForm.reset(); 

    loginForm.addEventListener("submit", function(event) {
        event.preventDefault(); 
        
        const formData = new FormData(loginForm);
        const tenDN = formData.get("tenDN");
        const mK = formData.get("mK");
        
        if (tenDN.trim() !== "" && mK.trim() !== "") {
            fetch(`/checklogin?tenDN=${tenDN}&mK=${mK}`, {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success && data.user_info) {
                    
                    localStorage.setItem('tenDN', tenDN);
                    localStorage.setItem('mK', mK);
                    // localStorage.setItem('idCanBo', data.user_info.idCanBo);
                    window.location.href = `/hethong?id=${data.user_info.idCanBo}`;
                } else {
                    alert("Đăng nhập không thành công. Vui lòng kiểm tra lại tên đăng nhập và mật khẩu.");
                }
            })
            .catch(error => {
                console.error('Lỗi khi gửi yêu cầu đăng nhập:', error);
            });
        } else {
            alert("Vui lòng nhập tên đăng nhập và mật khẩu.");
        }
    });
});
