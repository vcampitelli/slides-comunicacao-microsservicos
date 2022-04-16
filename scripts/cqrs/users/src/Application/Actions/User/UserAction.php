<?php

declare(strict_types=1);

namespace Users\Application\Actions\User;

use Framework\Application\Actions\Action;
use Framework\Application\Service\CommandBrokerInterface;
use Psr\Log\LoggerInterface;
use Users\Domain\User\UserQueryInterface;

abstract class UserAction extends Action
{

    /**
     * @var UserQueryInterface
     */
    protected UserQueryInterface $userQuery;

    /**
     * @param LoggerInterface $logger
     * @param CommandBrokerInterface $broker
     * @param UserQueryInterface $userQuery
     */
    public function __construct(
        LoggerInterface $logger,
        CommandBrokerInterface $broker,
        UserQueryInterface $userQuery
    ) {
        parent::__construct($logger, $broker);
        $this->userQuery = $userQuery;
    }

}
