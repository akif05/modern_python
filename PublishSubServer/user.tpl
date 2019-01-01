% rebase('base.tpl')
<div class="pure-g">
  <div calss="pure-u-724 userlist">
    <section>
    % include('single_user.tpl', user=user, comb=comb)
    </section>
  </div>

<div class="pure-u-1-24"> </div>

  <div class="pure-u-2-3 postlist">
    <section>
    <hr>
    <h2> {{heading}} </h2>
    <table class="pure-table pure-table-horizontal">
      % for posts in posts:
      %     post_user = comb.user_info[post.user]
      <tr>
        <td> {{post_user. displayname}} </td>
        <td> @{{post_user}} </td>
        <td> {{comb.age(post)}} </td>
        <td> {{post.text}} </td>
      </tr>
      % end
    </table> 
    </section>
  </div>
</div>
