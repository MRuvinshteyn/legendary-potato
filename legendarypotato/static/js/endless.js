var guessButton = document.getElementById('guess-button');
var subject = document.getElementById('subject').innerText;
var userid = document.getElementById('userid').innerText;
var qid = document.getElementById('question-id').innerText;

//console.log(qid);

function getNewQuestion(subject) {
  console.log('test');
  $.ajax({
    type: "POST",
    url: "/getquestion",
    data: {
      subject: subject
    },
    success: function(e) {
      //console.log(e);
      qid = document.getElementById('question-id').innerText = e.question_id;
      document.getElementById('question-img').src = e.question_img;
      document.getElementById('useranswer').value = '';
    },
  });
}

guessButton.addEventListener('click', function() {
  var useranswer = document.getElementById('useranswer').value;
  $.ajax({
    type: "POST",
    url: "/getanswer",
    data: {
      questionid: qid,
      userid: userid,
      useranswer: useranswer,
      subject: subject
    },
    success: function(e) {
      //console.log(e);
      document.getElementById('solution-pic').src = e.answer_img;
      document.getElementById('correct').innerText = (e.correct? "Correct!": "Incorrect");
      getNewQuestion(subject);
    },
  });
});
