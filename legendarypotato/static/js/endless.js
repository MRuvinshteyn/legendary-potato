var guessButton = document.getElementById('guess-button');
var qid = document.getElementById('question-id').innerText;

console.log(qid);

guessButton.addEventListener('click', function() {
  $.ajax({
    type: "POST",
    url: "/getquestion",
    data: {
      questionid: qid
    },
    success: function(e) {
      console.log(e);
    },
  });
});
