function updateTrashcanStatus() {
    $.get("/get_trash_value", function (data) {
        var trash1Value = data.trash1_value;

        // 更新垃圾桶状态
        var statusElement = document.getElementById("status1");
        statusElement.textContent = trash1Value + "%";

        // 根据垃圾桶值更新图像
        var imageElement = document.getElementById("trash1");
        if (trash1Value == 0) {
            imageElement.src = 'static/img/trash0.png';
        } else if (trash1Value > 0 && trash1Value <= 25) {
            imageElement.src = 'static/img/trash1.png';
        } else if (trash1Value > 25 && trash1Value <= 50) {
            imageElement.src = 'static/img/trash2.png';
        } else if (trash1Value > 50 && trash1Value <= 75) {
            imageElement.src = 'static/img/trash3.png';
        } else if (trash1Value > 75) {
            imageElement.src = 'static/img/trash4.png';
        }
    }).fail(function (error) {
        console.error("Error:", error);
    });
}

// 初始加载垃圾桶状态
updateTrashcanStatus();

// 每五秒更新一次垃圾桶状态
setInterval(updateTrashcanStatus, 1000);
