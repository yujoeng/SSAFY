<!DOCTYPE html>
<html lang="en">
<head>
  <title>Document</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <ul class="switcher">
    <li id="grayButton"></li>
    <li id="whiteButton"></li>
    <li id="navyButton"></li>
  </ul>
  
  <h1>Theme Switcher</h1>
  
  <p>테마 변경 기능 구현하기</p>

  <script>
    /* 
			- 각 li 태그가 클릭 되면 body의 background color 와 color 속성이 변경되어야 한다.
				- css와 HTML 마크업을 직접 수정하지 않는다.
      1. li#grayButton 클릭시 background-color는 gray, color는 white로 변경
      2. li#whiteButton 클릭시 background-color는 white, color는 black으로 변경
      3. li#navyButton 클릭시 background-color는 navy, color는 white로 변경
    */
   // 1. 필요한 요소 선택 (클래스는 . 아이디는 # 으로 선택)
    const grayButton = document.querySelector('#grayButton')     # HTML에서 id = 'grayButton' 인 li 요소 하나를 선택 
    const whiteButton = document.querySelector('#whiteButton')    # HTML에서 id = 'whiteButton' 인 li 요소 하나를 선택
    const navyButton = document.querySelector('#navyButton')      # HTML에서 id = 'navyButton' 인 li 요소 하나를 선택
    const body = document.body                                        # 현재 페이지의 body 요소를 바로 가져오기 
    
   // 2. 각 버튼에 클릭 이벤트 핸들러 등록

   // 회색 테마 
    grayButton.addEventListener('click', function(){       # addEventListener('click', 함수) -> 해당 요소 '클릭했을 때' 실행할 코드 등록
      body.style.backgroundColor = 'gray'
      body.style.color = 'white'
    })

    // 흰색 테마
    whiteButton.addEventListener('click', function(){     
      body.style.backgroundColor = 'white'
      body.style.color = 'black'
    })

    // 남색 테마 
    navyButton.addEventListener('click', function(){
      body.style.backgroundColor = 'navy'
      body.style.color = 'white'
    })

# body.style.backgroundColor / body.style.color  css를 직접 수정하지 않고, js로 인라인 스타일을 바꾸는 방식 
  
  </script>
</body>
</html>


