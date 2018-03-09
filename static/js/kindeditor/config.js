KindEditor.ready(function(K) {  
        K.create('textarea[name=content]',{
            width:800,  
            height:200,  
            uploadJson: '/admin/upload/kindeditor'  
        });  
});  