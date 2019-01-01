% rebase('base.tpl')
<div class="pure-g">
  <div class="pure-u-7-24 userlist">
    <section>
    % include('single_user.tpl', user=user, comb=comb)

    <hr>
    <h2> Post a new message </h2>
    <form class="pure-form" method="post" action="/postmessage">
      <input class="newpost" name="text" type="text">
      <button type="submit" class="pure-button-primary"> Post </button>
    </form>
    </section>
</div>

<div class="pure-u-1-24"> </div>

<div class="pure-u-2-3 postlist>
  <section>
  <hr>
  <h2> {{heading}} </h2>
  <table class="pure-table pure-table-horizontal">
  % for post in posts:
  %     post_user = comb.user_info[post.user]
  <tr>
