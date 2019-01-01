% rebase('base.tpl')

<section class="userlist">
  <h2> {{who_does_what}} </h2>
    % for user in users:
    %       include('single_user.tpl, user=user, comb=comb)
    % end
</section>
