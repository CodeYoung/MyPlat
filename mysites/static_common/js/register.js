document.getElementById("registerform").sumbit(function(){
//$("#registerform").sumbit(function(){
    alert("hello");
    var name=document.getElementById("usernamesignup");
    if(name.validity.valueMissing==true){
        name.setCustomValidity("用户名不能为空!");
        return;
    }
    else{
        name.setCustomValidity("");
    }
    var email=document.getElementById("emailsignup");//这个只能是document对象
    if(email.validity.valueMissing==true){
        email.setCustomValidity("邮箱不能为空!");
        return;
    }
    else{
        email.setCustomValidity("");
    }
    
    var pwd=document.getElementById("passwordsignup");
    if(pwd.validity.valueMissing==true){
        pwd.setCustomValidity("密码不能为空!");
        return;
    }
    else if(pwd.validity.patternMismatch==true){
        pwd.setCustomValidity("密码必须是6-20位的英文和数字！");
        return;
    }
    else{
        pwd.setCustomValidity("");
    }
    var rpwd=document.getElementById("passwordsignup_confirm");
    if(rpwd.validity.valueMissing==true){
        rpwd.setCustomValidity("密码不能为空!");
        return;
    }
    else if(rpwd.value!=pwd.value){
        rpwd.setCustomValidity("两次输入的密码不一样！");
        return;
    }
    else{
        rpwd.setCustomValidity("");
    }
    //var us=$("#email").val();
    //var u=new User($("#nickName").val(),$("#pwd").val(),us,$("#province").val()+$("#city").val(),$("input [name='sex']").val());
    //users[us]=[u];
})