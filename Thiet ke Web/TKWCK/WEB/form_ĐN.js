function kiemtra_ĐN() {
    var p1 = document.getElementById("username").value;
    var p2 = document.getElementById("password").value;


    if (p1 == "") {
        alert("Vui lòng nhập tên đăng nhập !");
    } else if (p2 == "") {
        alert("Vui lòng nhập mật khẩu !");
    } else {
        // alert("Xin hãy điền đúng thông tin !");
        return true;
    }
}