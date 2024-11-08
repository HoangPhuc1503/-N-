document.addEventListener('DOMContentLoaded', function() {
    
    


    fetch("/phanquyen_data")
    .then(response => response.json())
    .then(data => {
        const users = data.listCB;
        const permissions = data.listQTC;

        renderUsers(users);
        renderPermissions(permissions);
        console.log(data.listCB)
        console.log(data.listQTC)
    })
    .catch(error => {
        console.error("Lỗi khi lấy dữ liệu:", error);
    });
    
    
      function groupByDepartment(users) {
        return users.reduce((acc, user) => {
          const department = user.khoa;
          if (!acc[department]) {
            acc[department] = { name: department, children: [] };
          }
          acc[department].children.push({ id: user.id, name: user.name, khoa: user.khoa, quyen: user.quyen , chucvu: user.chucvu });
          return acc;
        }, {});
      }
      
      function groupList(users) {
        const Khoa = [];
        const DanhSach = { name: 'Danh Sách', children: [] };
        
        const group = groupByDepartment(users);
        users.forEach(item => {
          if (!Khoa.includes(item.khoa)) {
            Khoa.push(item.khoa);
          }
        });
      
        Khoa.forEach(item => {
          DanhSach.children.push(group[item]);
        });
        
        return [DanhSach];
      }
    

    const userList = document.getElementById('user-list');
    const permissionList = document.getElementById('permission-list');

    const searchUserInput = document.getElementById('search-user');
    const searchPermissionInput = document.getElementById('search-permission');

    function renderTreeView(data, parentElement) {
        const ul = document.createElement('ul');
        const permissionCheckbox = document.createElement('input');
        permissionCheckbox.type = 'checkbox';

        data.forEach(item => {
            const li = document.createElement('li');
            
            if (item.children && item.children.length > 0) {
                li.textContent = item.name;
                renderTreeView(item.children, li);
            } else {
                li.classList.add('leaf');
                const checkbox = document.createElement('input');
                checkbox.type = 'checkbox';
                checkbox.id = item.id;
                checkbox.value = item.name;
                li.textContent = ' ---  ' + item.name + ' - ' + item.chucvu  ; 
                li.addEventListener('click', () => {
                    alert('Nhân Viên: ' + item.name + "\nQuyền: " + item.quyen)
                });
                li.appendChild(checkbox);
                
            }
            ul.appendChild(li);
        });

        parentElement.appendChild(ul);
    }

    function renderUsers(users) {
        userList.innerHTML = '';
        users = groupList(users); 
        renderTreeView(users, userList);
    }

    function renderPermissions(permissions) {
        permissionList.innerHTML = '';
        permissions.forEach(permission => {
            const li = document.createElement('li');
            li.textContent = permission.name;
            li.dataset.permissionId = permission.id;
            li.addEventListener('click', () => {
                const selected = document.querySelector('.selected');
                if (selected) {
                    selected.classList.remove('selected');
                }
                li.classList.add('selected');
            });
            permissionList.appendChild(li);
        });
    }

    function filterList(list, query) {
        return list.filter(item => item.name.toLowerCase().includes(query.toLowerCase()));
    }

    searchUserInput.addEventListener('input', function() {
        const query = searchUserInput.value;
        const filteredUsers = filterList(users, query);
        renderUsers(filteredUsers);
    });

    searchPermissionInput.addEventListener('input', function() {
        const query = searchPermissionInput.value;
        const filteredPermissions = filterList(permissions, query);
        renderPermissions(filteredPermissions);
    });


    const assignPermissionButton = document.getElementById('assign-permission');

    assignPermissionButton.addEventListener('click', function() {
        const selectedUsers = document.querySelectorAll('input[type="checkbox"]:checked');
        const selectedPermissions = document.querySelectorAll('.selected');
        if (selectedUsers.length === 0 || selectedPermissions.length === 0) {
            alert('Vui lòng chọn người dùng và quyền cần phân quyền.');
            return;
        }
        selectedUsers.forEach(item =>{
            updatePermissions(item.id, selectedPermissions[0].dataset.permissionId);
        })
    });
});

async function updatePermissions(idCanBo, idQuyenTruyCap) {
    idCanBo = parseInt(idCanBo);
    idQuyenTruyCap = parseInt(idQuyenTruyCap);
    const response = await fetch(`/phanquyen_put/idCanBo=${idCanBo}&idQuyenTruyCap=${idQuyenTruyCap}`, {
        method: 'PUT',
    });
  
    if (response.ok) {
      // Request successful
      alert('Phân Quyền thành công');
      window.location.href = window.location.href;
      console.log("Permissions updated successfully!");
      // You can also update the UI to reflect the changes
    } else {
      // Request failed
      const error = await response.json();
      console.error("Error updating permissions:", error);
    }
}