//使用$替换document.getElementById函数
var $=function(v){return document.getElementById(v);}

/********验证用户输入******/
function ValidateInput(element,value){
	//验证密码
	if(element=="password"){
		if(value.toString().length<6){
			$('tipPosition').className='error';
			$('tipPosition').innerHTML="密码设置错误。密码长度过小。";
			return;
		}
		else{
			$('tipPosition').className='success';
			$('tipPosition').innerHTML="填写正确。";
		}
	}
}

/*======密码验证JS=====Begin======*/
//密码初始化的样式

function initCss(){
	$('tipPosition').className='tip';
	$('tipPosition').innerHTML="最小长度:。最大长度:16。";
}

/*======密码强度=====Begin=======*/

function Evaluate(word){
	return word.replace(/^([a-z])|([A-Z])|([0-9])|(.)){5,}|(.)+$/g, "$1$2$3$4$5").length;
}

function validatePwdStrong(value){
	var pwd={
		color:['#E6EAED','#AC0035','#FFCC33','#639BCC','#246626'],
		text:['太短','弱','一般','很好','极佳']
	};

	function colorInit(){
		$('pwdStrong_1').style.backgroundColor=pwd.color[0];
		$('pwdStrong_1').style.backgroundColor=pwd.color[0];
		$('pwdStrong_1').style.backgroundColor=pwd.color[0];
		$('pwdStrong_1').style.backgroundColor=pwd.color[0];
	}

	if(Evaluate(value)==1){
		colorInit();
		$('pwdStrong_1').style.backgroundColor=pwd.color[1];
		$('pwdStrong_text').innerHTML=pwd.text[1];
		$('pwdStrong_text').style.color=pwd.color[1];
	}
	else if(Evaluate(value)==2){
		colorInit();
		$('pwdStrong_1').style.backgroundColor=pwd.color[2];
		$('pwdStrong_2').style.backgroundColor=pwd.color[2];
		$('pwdStrong_text').innerHTML=pwd.text[2];
		$('pwdStrong_text').style.color=pwd.color[2];
	}
	else if (Evaluate(value) == 3) { 
		colorInit(); 
		$('pwdStrong_1').style.backgroundColor = pwd.color[3]; 
		$('pwdStrong_2').style.backgroundColor = pwd.color[3]; 
		$('pwdStrong_3').style.backgroundColor = pwd.color[3]; 
		$('pwdStrong_text').innerHTML = pwd.text[3]; 
		$('pwdStrong_text').style.color = pwd.color[3]; 
	} 
	else if (Evaluate(value) == 4) { 
		$('pwdStrong_1').style.backgroundColor = pwd.color[4]; 
		$('pwdStrong_2').style.backgroundColor = pwd.color[4]; 
		$('pwdStrong_3').style.backgroundColor = pwd.color[4]; 
		$('pwdStrong_4').style.backgroundColor = pwd.color[4]; 
		$('pwdStrong_text').innerHTML = pwd.text[4]; 
		$('pwdStrong_text').style.color = pwd.color[4]; 
	}
}