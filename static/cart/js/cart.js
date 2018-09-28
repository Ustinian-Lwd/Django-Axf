$(function () {
    $('.cart').width(innerWidth)


//    勾选的点击事件
    $('.cart .confirm-wrapper').click(function () {

        var cartid = $(this).attr('cartid')
        //get请求中  this
        var $that = $(this)

        $.get('/axf/changecartstatus/', {'cartid': cartid}, function (response) {
            // console.log(response)

            if (response['status'] == '1') {
                var isselect = response['isselect']
                $that.attr('isselect', isselect)
                // 先清空
                $that.children().remove()
                if (isselect) {  // 选中
                    $that.append('<span class="glyphicon glyphicon-ok"></span>')
                } else {    // 未选中
                    $that.append('<span class="no"></span>')
                }


                // 总计
                total()


//####################################################33

                // var total_price = 0
                // console.log(123)
                // // 遍历
                // $('.goods').each(function () {
                //     console.log(456)
                //     //用来判断是否呗选中了
                //     var $confirm = $(this).find('.confirm-wrapper')
                //     //获取到其中的内容
                //     //数量
                //     //价格
                //     var $content = $(this).find('.content-wrapper')
                //
                //     // 选中，才计算
                //     if ($confirm.find('.glyphicon-ok').length) {
                //         console.log(2)
                //         var price = parseInt($content.find('.price').attr('str_price'))
                //         var num = parseInt($content.find('.num').attr('str_num'))
                //         total_price += num * price
                //     }
                // })
                // // 修改总计 显示
                // $('.bill .total b').html(total_price)


//####################################################33


            }
        })
    })


//    全选的点击事件
    $('.cart .bill .all').on('click', function () {
        var isall = $(this).attr('isall')
        isall = (isall == 0) ? 1 : 0
        // isall = !isall
        $(this).attr('isall', isall)


        // 自身状态
        //将全选删除掉
        $(this).children().remove()
        if (isall) { // 全选
            $(this).append('<span class="glyphicon glyphicon-ok"></span>').append('<b>全选</b>')
        } else {    // 取消全选
            $(this).append('<span class="no"></span>').append('<b>全选</b>')
        }

        // 发起ajax请求
        $.get('/axf/changecartselect/', {'isall': isall}, function (response) {
            console.log(response)
            if (response['status'] == '1') {
                // 遍历
                $('.confirm-wrapper').each(function () {
                    $(this).attr('isselect', isall)
                    $(this).children().remove()
                    if (isall) { // 选中
                        $(this).append('<span class="glyphicon glyphicon-ok"></span>')
                    } else {    // 未选中
                        $(this).append('<span class="no"></span>')
                    }
                })

                //    总计
                total()
                // console.log(total())


//####################################################33

                // var total_price = 0
                //
                // // 遍历
                // $('.goods').each(function () {
                //     console.log(1)
                //     //用来判断是否呗选中了
                //     var $confirm = $(this).find('.confirm-wrapper')
                //     //获取到其中的内容
                //     //数量
                //     //价格
                //     var $content = $(this).find('.content-wrapper')
                //
                //     // 选中，才计算
                //     if ($confirm.find('.glyphicon-ok').length) {
                //         console.log(2)
                //         var price = parseInt($content.find('.price').attr('str_price'))
                //         var num = parseInt($content.find('.num').attr('str_num'))
                //         total_price += num * price
                //     }
                // })
                // // 修改总计 显示
                // $('.bill .total b').html(total_price)


//####################################################33


            }
            //    发送的ajax
        })
        //    全选的点击事件
    })


    // 计算总价格
    function total() {
        var total_price = 0

        // 遍历
        $('.goods').each(function () {
            //用来判断是否呗选中了
            var $confirm = $(this).find('.confirm-wrapper')
            //获取到其中的内容
            //数量
            //价格
            var $content = $(this).find('.content-wrapper')

            // 选中，才计算
            if ($confirm.find('.glyphicon-ok').length) {
                var price = ($content.find('.price').attr('str_price'))
                var num = parseInt($content.find('.num').attr('str_num'))
                total_price += num * price

            }
        })

        // 保留两位小数
        total_price = Fractional(total_price)

        // 修改总计 显示
        $('.bill .total b').html(total_price)
    }


        //小数位数的处理
        //小数位数控制，可以四舍五入
    function Fractional(n) {
        //小数保留位数
        var bit = 2;
        //加上小数点后要扩充1位
        bit++;
        //数字转为字符串
        n = n.toString();
        //获取小数点位置
        var point = n.indexOf('.');
        //n的长度大于保留位数长度
        if (n.length > point + bit) {
        //保留小数后一位是否大于4，大于4进位
            if (parseInt(n.substring(point + bit, point + bit + 1)) > 4) {
                return n.substring(0, point) + "." + (parseInt(n.substring(point + 1, point + bit)) + 1);
            }
            else {
                return n.substring(0, point) + n.substring(point, point + bit);
            }
        }
        return n;
    }









})