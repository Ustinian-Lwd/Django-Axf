$(function () {
    //隐藏滚动条
    $('.register').width(innerWidth)

//    用户名
// 　失去焦点
    $('#account').on('blur', function () {

        $.get('/axf/checkuser/', {'account': $(this).val()}, function (response) {
            //测验ajax请求是否成功发起
            // console.log(response)
            // 数据连接成功！！

            //    若status==-1
            if (response['status'] == -1) {
                $('#accounterr').show().html(response['msg'])
            }
            else {
                $('#accounterr').hide()
            }

        })
    })

    //    密码
    //    失去焦点
        $('#password').on('blur', function () {

        //    获取输入框的值
        //    判断密码符不符合要求
        //     var password = $(this).val()
        //     if(password.length<6 || password.length>12){
        //         $('#passworderr').show()
        //     } else {
        //         $('#passworderr').hide()
        //     }

            var password = $(this).val()
            //如果密码为空
            if(password == '' ){
                $('#passworderr').show().html('密码不为空')
            }
            else if(password != ''){
                if(password.length<6 || password.length>12) {
                    $('#passworderr').show().html('请输入６~12位数')
                }
                else{
                     $('#passworderr').hide()
                }
            }



        })


    //    确认密码
    //    失去焦点
        $('#mypassword').on('blur', function () {

            // var mypassword = $(this).val()
            // if (mypassword != password){
            //      $('#mypassworderr').show()
            // }
            // else{
            //     $('mypassworderr').hide()
            // }

            var mypassword = $(this).val()

            // 如果确认密码为空
            if(mypassword == ''){
                $('#mypassworderr').show().html('请再一次输入密码')
            }
            //密码不为空
            else if(mypassword != ''){
                if (mypassword != $('#password').val()){
                    $('#mypassworderr').show().html("密码不匹配")
                }
                else{
                    $('mypassworderr').hide()
                }

            }




        })




})