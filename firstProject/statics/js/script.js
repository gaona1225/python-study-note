function getCookie(name){
	var x = document.cookie.match("\\b" + name + "=([^;]*)\\b");
	return x ? x[1]:undefined
}

$(function(){
	$("#login").click(function(){
		var user = $("#username").val();
		var pwd = $("#password").val();
		var pd = {"username":user,"password":pwd,"_xsrf":getCookie("_xsrf")};
		$.ajax({
			url:"/",
			type:"post",
			data:pd,
			cache:false,
			success:function(rsp){
				console.log("success");
				console.log(rsp);
				window.location.href = "/user?user="+rsp
			},
			error:function(){
				console.log("error");
			}
		})
	})
});