/**
 * 제공 코드
 */
// 기본 영화 데이터 (JavaScript Array)
const genres = genreRawData
const movies = movieRawData
// 데이터 확인
console.log(genres.length)
console.log(genres[0])
console.log(movies.length)
console.log(movies[0])

/**
 * 대부분의 작업은 script.js에서 진행해도 무방하나 원한다면 js 파일 추가 가능
 * HTML 요소 추가를 위한 `.innerHTML` 사용 금지, 요소의 내용을 비우는 용도로는 사용 가능 (`.innerHTML = ```)
 */

//DOM 요소 가져오기 
const movieListSection = document.querySelector('#movie-list-section')
const genreFilterSection = document.querySelector('#movie-genre-filter')
const movieFormSection = document.querySelector('#movie-form-section')

// 화면에서 사용할 상태 
// 원본 데이터에 id 추가
let movieState = movies.map((m, index) => ({ 
  ...m, 
  id: index + 1 
}))
let currentGenreId = 'all'

// 새로운 영화 id 자동 증가 계산 
let nextMovieId = movieState.length
  ? Math.max(...movieState.map(m => m.id)) + 1
  : 1
  
// 영화 목록 출력을 위한 ul 생성
const movieListUL = document.createElement('ul')
movieListUL.classList.add('list-group')
movieListSection.appendChild(movieListUL)
  
// 영화 목록 렌더링
function getFilteredMovies(){
  if (currentGenreId === 'all') return movieState

  const gid = Number(currentGenreId)
  return movieState.filter(movie => movie.genres.includes(gid))
}

function renderMovieList() {
  // 목록 비우기 
  movieListUL.innerHTML = ''

  const filtered = getFilteredMovies()

  filtered.forEach(movie => {
    const li = document.createElement('li')
    li.classList.add('list-group-item', 'd-flex', 'justify-content-between', 'align-items-center')
    li.textContent = movie.title
    
    // 삭제 버튼
    const btn = document.createElement('button')
    btn.type = 'button'
    btn.classList.add('btn', 'btn-danger', 'btn-sm')
    btn.textContent = '삭제'
    btn.addEventListener('click', () => deleteMovie(movie.id))
    
    li.appendChild(btn)
    movieListUL.appendChild(li)
  })
}

// 장르 선택을 위한 select 생성 및 필터링 기능 구현
let genreSelectElement = null

function initGenreFilter() {
    const label = document.createElement('label')
    label.setAttribute('for', 'genre-filter-select')
    label.textContent = '장르 선택: '
    label.classList.add('form-label', 'mt-3')

    const select = document.createElement('select')
    select.id = 'genre-filter-select'
    select.classList.add('form-select', 'mb-3')

    // 전체 보기 옵션
    const allOption = document.createElement('option')
    allOption.value = 'all'
    allOption.textContent = '전체'
    select.appendChild(allOption)

    // 장르 옵션 목록
    genres.forEach(g => {
        const option = document.createElement('option')
        option.value = g.id
        option.textContent = g.name
        select.appendChild(option)
    })

    select.addEventListener('change', e => {
        currentGenreId = e.target.value
        renderMovieList()
    })

    genreFilterSection.appendChild(label)
    genreFilterSection.appendChild(select)

    genreSelectElement = select
}

// 영화 추가 기능 UI 구현
let formGenreSelectElement = null
let titleInputElement = null

function initMovieForm() {
    const form = document.createElement('form')
    form.classList.add('mt-3')

    // 제목 입력창
    const titleLabel = document.createElement('label')
    titleLabel.textContent = '영화 제목'
    titleLabel.classList.add('form-label')
    
    const titleInput = document.createElement('input')
    titleInput.type = 'text'
    titleInput.placeholder = '영화 제목을 입력하세요'
    titleInput.classList.add('form-control', 'mb-3')

    // 장르 선택 라벨
    const genreLabel = document.createElement('label')
    genreLabel.textContent = '장르'
    genreLabel.classList.add('form-label')
    
    // 장르 선택
    const genreSelect = document.createElement('select')
    genreSelect.classList.add('form-select', 'mb-3')

    const placeholder = document.createElement('option')
    placeholder.value = ''
    placeholder.textContent = '장르 선택'
    placeholder.selected = true
    placeholder.disabled = true
    genreSelect.appendChild(placeholder)

    genres.forEach(g => {
        const opt = document.createElement('option')
        opt.value = g.id
        opt.textContent = g.name
        genreSelect.appendChild(opt)
    })

    // 제출용 버튼 생성
    const btn = document.createElement('button')
    btn.type = 'submit'
    btn.textContent = '추가'
    btn.classList.add('btn', 'btn-primary')

    form.addEventListener('submit', handleMovieSubmit)

    // form에 요소 추가
    form.appendChild(titleLabel)
    form.appendChild(titleInput)
    form.appendChild(genreLabel)
    form.appendChild(genreSelect)
    form.appendChild(btn)
    
    movieFormSection.appendChild(form)

    titleInputElement = titleInput
    formGenreSelectElement = genreSelect
}

function handleMovieSubmit(event) {
  event.preventDefault()

  const title = titleInputElement.value.trim()
  const genreId = formGenreSelectElement.value

  if (!title) {
    alert('제목을 입력하세요')
    return
  }
  if (!genreId) {
    alert('장르를 선택하세요')
    return
  }

  const newMovie = {
    id: nextMovieId++,
    title,
    genres: [Number(genreId)],
    description: '',
    posterPath: ''
  }

  // 목록 최상단에 추가
  movieState.unshift(newMovie)

  // 입력 초기화
  titleInputElement.value = ''
  formGenreSelectElement.value = ''

  // 장르 필터를 전체로 변경
  currentGenreId = 'all'
  genreSelectElement.value = 'all'

  renderMovieList()
}

function deleteMovie(movieId) {
    movieState = movieState.filter(m => m.id !== movieId)
    renderMovieList()
}

// 초기 실행
function init() {
    initGenreFilter()
    initMovieForm()
    renderMovieList()
}

document.addEventListener('DOMContentLoaded', init)