# 21. Code based grading

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287737
**Section:** 04 Prompt evaluation

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                                
                                    
                                    1
                                    download
                                
                            
                        
                    
                
            
            
                
                
                
                    Code based grading
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                When evaluating AI models that generate code, you need more than just checking if the response makes sense. You also need to verify that the generated code actually has valid syntax and follows the correct format. This is where code-based grading comes in.

How Code Grading Works

Code grading validates two key aspects of AI-generated responses:

Format - The response should return only the requested code type (Python, JSON, or Regex) without explanations
Valid Syntax - The generated code should actually parse correctly as the intended language
Task Following - The response should directly address what was asked and be accurate

The first two criteria are handled by the code grader, while task following is evaluated by the model grader. Together, they provide a comprehensive evaluation.

Syntax Validation Functions

To check if generated code has valid syntax, you can create three helper functions that attempt to parse the output:

def validate_json(text):
    try:
        json.loads(text.strip())
        return 10
    except json.JSONDecodeError:
        return 0

def validate_python(text):
    try:
        ast.parse(text.strip())
        return 10
    except SyntaxError:
        return 0

def validate_regex(text):
    try:
        re.compile(text.strip())
        return 10
    except re.error:
        return 0

Each function tries to parse the text as its respective format. If parsing succeeds, it returns a perfect score of 10. If it fails with an error, the syntax is invalid and returns 0.

Dataset Format Requirements

For the code grader to know which validator to use, your test cases need to specify the expected output format:

{
    "task": "Create a Python function to validate an AWS IAM username",
    "format": "python"
}

You can update your dataset generation prompt to automatically include this format field by adding it to the example output structure.

Improving Prompt Clarity

To get better results from your AI model, make your prompt instructions more specific about the expected output format:

* Respond only with Python, JSON, or a plain Regex
* Do not add any comments or commentary or explanation

You can also use a pre-filled assistant message with code blocks to encourage the model to return just the raw code:

add_assistant_message(messages, "```code")

This tells Claude to start generating code content without having to specify whether it's Python, JSON, or Regex ahead of time.

Combining Scores

The final step is merging the model grader score with the code grader score. A simple approach is to take the average:

model_grade = grade_by_model(test_case, output)
model_score = model_grade["score"]
syntax_score = grade_syntax(output, test_case)

score = (model_score + syntax_score) / 2

This gives equal weight to both content quality and technical correctness. You might adjust these weights based on what matters more for your specific use case.

Testing Your Implementation

Once you've implemented code grading, run your evaluation to get a baseline score. The score itself isn't inherently good or bad - what matters is whether you can improve it by refining your prompts. This gives you a quantitative way to measure prompt engineering progress rather than relying on subjective assessment.
                            
                        
                    

                    
                        
                            Downloads
                            
                                
                                    
                                        
                                            
                                            
                                                001_prompt_evals_fns.ipynb
                                                (opens in new tab)

---

## 🎬 Transcript (English)

Next up, we need to implement our code grader. So our code grader is going to take in some output from the model and make sure that we get back just plain Python, JSON, or regular expression without any kind of explanation. In addition, we should also make sure that we have valid syntax for whatever type of code we actually got. You might be kind of curious, how are we going to validate the syntax of, say, Python at all? Well, we use a little trick for this. We're going to define three helper functions, one will be called Validate JSON, another Validate Python, and another Validate Reg X. Then inside of each of those, we're going to take whatever output we got from the model and try to either parse it as JSON, we'll try to parse it as a Python abstract syntax tree or AST, or we'll try to compile it as a regular expression. And for each of these, if we successfully parse or load or whatever else, we'll return a full score of 10. Otherwise, if we get an error during this parsing operation, we'll assume that we completely failed the syntax check and return a zero. There is one other thing to be aware of here. In order to know which of these different validators or these kind of grading functions to run, we need our test case data set to include the expected format that we're going to get back for each output. So in other words, back here inside of our data set, On our first task, for me, at least, I was expecting to get back a Python function and then JSON and then a reg X. So we need to update our data set to include something like a format key that will say, hey, this output should probably be Python. This one should be JSON and this one a reg X. Now, of course, I could just edit this file manually, but instead, we will update our prompt that is generating our data set so that we can eventually generate really large data sets for testing purposes. Now, total to do all this stuff, couple of different steps we have to go through. So just to help you understand the code side of it and keep everything in line, I came up with this quick checklist of items that we're going to go through. So our first item, adding functions to validate JSON, Python, and regular expressions. For this, I'm going to flip back over to my notebook. I'm going to find the run test case cell. I'm going to add a new cell right above it. And then inside there, I'm going to add those three functions you just saw inside that diagram. Once again, to save a little bit of time, I'm going to paste them in here. You can always copy the completed code out of the finished version of this notebook. So at the top of the cell, I'm importing these two helper modules. I've then got the three different validator functions we just saw. And then at the bottom, I have kind of a general purpose function to figure out which these different validators to use. So I've got grade syntax right here. That's going to take a look at the test case. It's going to look at the format in particular. So we need to make sure our test cases have that format property that I just mentioned a moment ago. And then depending upon that, we're going to call the appropriate format function. Okay, that is step one. Now step two, we need to update our data set to make sure we include that format key. So for that, we'll scroll up a little bit and find our data set. Here it is right here. So generate data set and I'm going to add onto the example output. On task, I'm gonna add a comma at the very end and I'll add in a format key And inside of here, we'll say simply JSON or Python or RegX. That's really all we have to do. So now if I rerun that cell and rerun the cell underneath it that actually generates the data set, there we go. Now we'll go back over to my data set file. And I'll see, yes, I did, in fact, get the format inside there. And it looks like it matches up with the task perfectly. So the first task is create a JSON configuration, got JSON, write Python, got Python, and then write a regular expression, and I got regx. OK, on to step number three. Now this, we're going to update our draft prompt template, just to make sure that it's really clear that we only want JSON Python or regular expression. Because right now, our draft prompt just kind of says, yeah, try to solve the task. So inevitably, we're going to get back some non JSON or non Python content and we'll always be failing the actual validation check. So we're just going to give our prompt a little help here, give it some work that we know that it needs. So for step three, will go back down to our run prompt, which is where our draft prompt is. And I'm going to update the prompt just a little bit. I'm going to add in some notes, and I'll ask it to respond only with Python, JSON, or a plain regX. And do not add any comments, or commentary, or explanation. Next up, I'm going to make sure that we get back just that raw content that we really care about. And once again, to do so, we'll use a prefilled assistant message along with a stop sequence. So I'll add in a assistant message right here. In my assistant message, in this case, I can put in three backticks, and then usually, as we saw previously, we might put in something like JSON or Bash or Python right here. But in this particular case, we don't really know ahead of time the exact format that we expect to get back. We don't know if we're going to get back Python or JSON or RegX. So one little cheat code here, one little work around, we could just put in code and that kind of pre-fills the assistant message and tells Claude, hey, you're going to put some code inside of here without us having to specifically say this is going to be Python or JSON or reg X. I'm then going to add on the closing stop sequence with backticks like so. Lastly, we need to actually merge the scores from our model grader and the code grader together. So for that back over here, I'm going to scroll down once again, and we will find our run test case function. So this is where we are running our model grader right underneath it. I'm going to put together the syntax grader per code grader, whichever you want to call it. So I'll say my syntax score is grade syntax. We need to pass in the output. and our test case. And then finally, we're going to merge the syntax score together with the model score. I'm going to first rename score right here to model score, just to be clear. And I'm going to take the average of these two scores. So I'll say score is going to be model score plus syntax score divided by two. And that should be it. So that's all it took to add in a little bit of code grading. So last thing to do is test this all out. To do so, we'll go down just a little bit here. So right underneath the runeval function is where we actually call runeval and calculate our overall average score. So I'm going to rerun this and remember it usually takes a decent number of seconds to complete. And after a short pause, I get a final score of 8.166. So now the question is, is this good or not? Well, the real answer to that is that we just don't know. The only way we're going to know is if we now try to change our prompt in somebody and hopefully get a better score. So let's try out an exercise in the next video where we will try to change our prompt a little bit and hopefully improve our score.

---

## 🎬 トランスクリプト（日本語）

次に、コードグレ―ダ―を実装する必要があります。 このコードグレ―ダ―は、モデルからの出力を受け取り、 プレーンなPython、 JSON、または正規表現のみを返すようにします。説明は含みません。 さらに、実際に受け取ったコードのタイプに対して、 有効な構文であることも確認する必要があります。 例えば、Pythonの構文をどのように検証するか、 疑問に思っているかもしれません。それは、 ちょっとしたトリックを使います。3つのヘルパー関数を定義します。 1つはValidate JSON、 もう1つはValidate Python、 さらにValidate Reg Xと呼びます。 そして、それぞれの中で、モデルから受け取った出力を JSONとしてパースするか、 Pythonの抽象構文ツリー（AST）としてパースするか、 または正規表現としてコンパイルするかを試みます。 そして、これらのそれぞれで、 パースまたはロードまたは、 その他の処理を成功させた場合、満点の10を返します。 それ以外の場合、このパース処理中にエラーが発生した場合、 構文チェックに完全に失敗したとみなし、 0を返します。ここで注意すべき点がもう一つあります。 これらの異なるバリデーターや、 これらの種別のグレ―ディング関数を実行するかを 知るためには、テストケースデータセットに、 各出力で取得することが期待されるフォーマットを含める必要があります。 つまり、言い換えると、データセット内のどこかに、 少なくとも私の最初のタスクでは、 Python関数、次にJSON、 そして正規表現を取得することを期待していました。 したがって、フォーマットキーのようなものを 含めるようにデータセットを更新する必要があります。 これはPythonであるべきだ、これはJSONであるべきだ、 そしてこれは正規表現であるべきだ、と。 もちろん、このファイルを手動で編集することもできますが、 代わりに、データセットを生成しているプロンプトを更新して、 最終的にテスト目的で非常に大規模な データセットを生成できるようにします。 これらすべてを行うために、いくつかの異なるステップがあります。 コード側を理解しやすくし、 すべてを整列させるために、これらの項目を すぐに確認できるチェックリストを作成しました。 最初の項目は、JSON、Python、 および正規表現を検証する関数を追加することです。 これを行うために、ノートブックに戻ります。 テストケースの実行セルを見つけて、 そのすぐ上に新しいセルを追加します。 そしてその中に、その図で見た3つの関数を追加します。 繰り返しますが、時間を節約するために、 ここに貼り付けます。完成版の ノートブックから完成したコードをコピーすることができます。 セルの先頭には、これらの2つのヘルパーモジュールをインポートしています。 そして、先ほど見た3つの異なるバリデーター関数があります。 そして下部には、これらの異なるバリデーターの どれを使用するかを判断するための汎用的な関数があります。 例えば、構文グレ―ディングがあります。 これはテストケースを見ます。 特にフォーマットを見ます。ですので、テストケースに 先ほど申し上げたフォーマットプロパティがあることを 確認する必要があります。そして、それに従って、 適切なフォーマット関数を呼び出します。 これがステップ1です。ステップ2は、 フォーマットキーを含めるために、 データセットを更新する必要があることです。 これを行うために、少し上にスクロールします。 そして、データセットを見つけます。 ここにあります。データセットの生成で、 タスクの例出力に追加します。 末尾にコンマを追加し、フォーマットキーを追加します。 そしてここに、JSON、 またはPython、 または正規表現とシンプルに記述します。 それがすべてです。したがって、 今、そのセルを再実行して、 実際にデータセットを生成する下のセルを 再実行すると、はい、うまくいきました。 データセットファイルに戻ってみます。 はい、ここにフォーマットが含まれていることがわかります。 そして、タスクに完全に一致しているようです。 最初のタスクはJSON設定の作成、JSONを取得しました。 Pythonを書き、Pythonを取得しました。 そして正規表現を書き、正規表現を取得しました。 ステップ3に進みます。 ここでは、ドラフトプロンプトテンプレートを更新します。 JSON、Python、 または正規表現のみを求めることを明確にするためです。 なぜなら、現時点では、ドラフトプロンプトは単にタスクを解決しようと 言っているだけだからです。 必然的に、JSONでもPythonでもないコンテンツが返ってきて、 常に検証チェックに失敗することになります。 したがって、プロンプトに少しヘルプを与え、 それが必要だとわかっている作業を与えます。 ステップ3では、ドラフトプロンプトがある 実行プロンプトまで下にスクロールします。 そしてプロンプトを少し更新します。注釈を追加し、 Python、JSON、 またはプレーンな正規表現のみで応答するように依頼します。 そして、コメント、 または解説、 または説明は追加しないでください。 次に、私たちが本当に気にしている その生のコンテンツのみを取得するようにします。 そして、これを実現するためにも、 事前入力されたアシスタントメッセージと ストップシーケンスを使用します。 ここに追加します。 この場合のアシスタントメッセージには、 3つのバッククォートを入れることができます。そして通常、 以前見たように、 JSONや BashやPythonなどをここに入れるかもしれません。 しかし、今回は、期待される 正確なフォーマットを事前に知ることはできません。 Python、JSON、または正規表現を取得するかわかりません。 そこで、ちょっとしたトリック、 回避策として、コードと入力することができます。 これはアシスタントメッセージを事前入力し、 Claudeに、PythonやJSON、 または正規表現であると具体的に言う必要なしに、 コードを入力することになります。 そして、このように閉じバッククォートで 終了ストップシーケンスを追加します。 最後に、モデルグレ―ダ―とコード グレ―ダ―のスコアを実際に結合する必要があります。 そのため、もう一度ここにスクロールして、 実行テストケース関数を見つけます。 ここでモデルグレ―ダ―を実行しています。 そのすぐ下に、構文グレ―ダ―、 コードグレ―ダ―とでも呼びましょうか。 私の構文スコアは `grade_syntax`です。 出力と テストケースを渡す必要があります。 そして最後に、構文スコアとモデル スコアを結合します。まず、 ここにあるスコアをモデルスコアに変更します。 そして、これらの2つのスコアの平均を取ります。 スコアは (モデルスコア + 構文スコア) / 2 になります。これで完了です。 コードグレ―ディングを追加するのはこれだけです。 最後にすべてをテストします。 これを行うために、もう少し下にスクロールします。 runeval関数を呼び出して 全体の平均スコアを計算する場所の すぐ下にあります。これを再実行して、 通常、完了するのにかなりの時間がかかることを覚えておいてください。 しばらくすると、最終スコア8.166が得られました。 さて、問題は、これは良いのか悪いのかということです。 本当の答えは、まだわからないということです。 わかる唯一の方法は、プロンプトをいくつか変更して、 より良いスコアを得ることです。 次のビデオでは、 プロンプトを少し変更して、スコアを改善しようとする 演習をしてみましょう。
