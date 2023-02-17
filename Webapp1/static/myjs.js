$(function() {
 $('.slide').each(function() {
   // スライド（画像）の数を取得
   var $slides = $(this).find('img'),
       slideNum = $slides.length,
       idx = 0; // 何番目か
 
   // idx番目目の画像をフェードイン
   $(".slide img").eq(idx).fadeIn();
 });
});
$(function() {
    $('.slide').each(function() {
      // スライド（画像）の数を取得
      var $slides = $(this).find('img'),
          slideNum = $slides.length,
          currentIdx = 0; // 何番目か
    
      // 最初の画像をフェードイン
      $(".slide img").eq(currentIdx).fadeIn();
    
      // 3秒後に次のスライドを表示
      setTimeout(dispNextSlide, 3000);
    
      // 次のスライドを表示するメソッド
      function dispNextSlide() {
        var nextIdx = currentIdx + 1;
    
        // 最後のスライドの場合ははじめに戻る
        if (nextIdx > (slideNum - 1)) {
          nextIdx = 0
        }
    
        // 現在のスライドをフェードアウト
        $(".slide img").eq(currentIdx).fadeOut();
    
        // 次のスライドをフェードイン
        $(".slide img").eq(nextIdx).fadeIn();
    
        // インデックスを更新
        currentIdx = nextIdx;
      }
    });
   });