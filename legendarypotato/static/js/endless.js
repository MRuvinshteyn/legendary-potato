var guessButton = document.getElementById('guess-button');
var qid = document.getElementById('question-id').innerText;

console.log(qid);

guessButton.addEventListener('click', function() {
  var useranswer = document.getElementById('useranswer').value;
  $.ajax({
    type: "POST",
    url: "/getanswer",
    data: {
      questionid: qid,
      useranswer: useranswer
    },
    success: function(e) {
      console.log(e);
      document.getElementById('solution-pic').src = e.answer_img;
    },
  });
});
