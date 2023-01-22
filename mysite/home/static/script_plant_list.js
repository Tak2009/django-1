//パノラマ初期設定
pannellum.viewer('panorama', {
    "type": "equirectangular",
    "panorama": "../static/img/360-view-trees.jpeg", // 最初に表示する画像
    "autoLoad": true
  });
  
  // サムネイルをクリックしたときの挙動
  $('.panorama-navs a').on('click', function() {
    $('#panorama').html('');
    var url = $(this).attr('data-item-url');
    pannellum.viewer('panorama', {
      "type": "equirectangular",
      "panorama": url,
      "autoLoad": true
    });
    return false;
  });