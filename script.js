$(function() {

    const token = "IGQVJXaDdlODF1cUJXVF9nakJ0cGx3aDB3WVV5OTJOLVZAMUmlpcnRBcW1NZA0YtM1FyLVN1NzZAHd21fSGJqSzhkUnAwcVpSd1d4ZA3dqYUI2LVpjQ2pYZAThHSHprWlFoUVRwMWZABNEVR";
    const url = "https://graph.instagram.com/me/media?access_token=" + token + "&fields=media_url,media_type,caption,permalink";

    $.get(url).then(function(response) {
        console.log('retorno: ', response.data);
        let dadosJson = response.data
        let contenido = '<div class="portafolio" style"padding-left:5px">';

        for(let p=0; p < dadosJson.length; p++){
            let feed = dadosJson[p];
            let titulo = feed.caption !== null ? feed.caption: '';
            let tipo = feed.media_type;
            if(tipo === 'VIDEO') {
                contenido += '<div class="col-12 col-sm-6 col-md-4 col-lg-4 col-xl-4 col-xxl-4"><video style="width:100%;height:90%" controls><source src="'+feed.media_url+'" type="video/mp4"></video></div>';
            }
            else if (tipo === 'IMAGE'){
                contenido += '<div class="col-12 col-sm-6 col-md-4 col-lg-4 col-xl-4 col-xxl-4"><img style="width:100%;height:90%" title="'+titulo+'" alt="'+titulo+'" src="'+feed.media_url+'" onclick="window.open(\''+feed.permalink+'\');"></div>';
            }
        }
        contenido += '</div>';
        $('#contenedor_ig').html(contenido);
    })

});