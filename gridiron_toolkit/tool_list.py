tools = [
    {
        "name": "get_player_info_tool",
        "description": "Fetch basic information for players such as: name, latest team, position, height, weight, birthdate (age) and identifiers",
        "inputSchema": {
            "type": "object",
            "properties": {
                "player_names": {
                    "items": {"type": "string"},
                    "title": "Player Names",
                    "type": "array",
                }
            },
            "required": ["player_names"],
        },
        "outputSchema": {
            "type": "object",
            "properties": {
                "result": {
                    "items": {"additionalProperties": true, "type": "object"},
                    "title": "Result",
                    "type": "array",
                }
            },
            "required": ["result"],
            "title": "_WrappedResult",
            "x-fastmcp-wrap-result": true,
        },
        "_meta": {"_fastmcp": {"tags": []}},
    },
    {
        "name": "get_players_by_sleeper_id_tool",
        "description": "Fetch basic information for players by their Sleeper IDs.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "sleeper_ids": {
                    "items": {"type": "string"},
                    "title": "Sleeper Ids",
                    "type": "array",
                }
            },
            "required": ["sleeper_ids"],
        },
        "outputSchema": {
            "type": "object",
            "properties": {
                "result": {
                    "items": {"additionalProperties": true, "type": "object"},
                    "title": "Result",
                    "type": "array",
                }
            },
            "required": ["result"],
            "title": "_WrappedResult",
            "x-fastmcp-wrap-result": true,
        },
        "_meta": {"_fastmcp": {"tags": []}},
    },
    {
        "name": "get_fantasy_rank_page_types",
        "description": "Get distinct dynasty rank page types for context. Returns a list of unique page_type values from vw_dynasty_ranks.",
        "inputSchema": {"type": "object", "properties": {}},
        "outputSchema": {
            "type": "object",
            "properties": {
                "result": {
                    "items": {"type": "string"},
                    "title": "Result",
                    "type": "array",
                }
            },
            "required": ["result"],
            "title": "_WrappedResult",
            "x-fastmcp-wrap-result": true,
        },
        "_meta": {"_fastmcp": {"tags": []}},
    },
    {
        "name": "get_fantasy_ranks",
        "description": "Fetch dynasty ranks from vw_dynasty_ranks, filtered by position and/or page_type (optional). Accepts an optional `limit` (default 30) to control rows returned. Returns the most pertinent columns for fantasy analysis.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "position": {
                    "anyOf": [{"type": "string"}, {"type": "null"}],
                    "default": null,
                    "title": "Position",
                },
                "page_type": {
                    "anyOf": [{"type": "string"}, {"type": "null"}],
                    "default": null,
                    "title": "Page Type",
                },
                "limit": {
                    "anyOf": [{"type": "integer"}, {"type": "null"}],
                    "default": 30,
                    "title": "Limit",
                },
            },
        },
        "outputSchema": {
            "type": "object",
            "properties": {
                "result": {
                    "items": {"additionalProperties": true, "type": "object"},
                    "title": "Result",
                    "type": "array",
                }
            },
            "required": ["result"],
            "title": "_WrappedResult",
            "x-fastmcp-wrap-result": true,
        },
        "_meta": {"_fastmcp": {"tags": []}},
    },
    {
        "name": "get_sleeper_leagues_by_username",
        "description": "Fetch sleeper leagues for a specific user by their username. Returns a filtered list of league objects. If verbose is True, includes scoring_settings, settings, and roster_positions.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "username": {"title": "Username", "type": "string"},
                "verbose": {"default": false, "title": "Verbose", "type": "boolean"},
            },
            "required": ["username"],
        },
        "outputSchema": {
            "type": "object",
            "properties": {
                "result": {
                    "items": {"additionalProperties": true, "type": "object"},
                    "title": "Result",
                    "type": "array",
                }
            },
            "required": ["result"],
            "title": "_WrappedResult",
            "x-fastmcp-wrap-result": true,
        },
        "_meta": {"_fastmcp": {"tags": []}},
    },
    {
        "name": "get_sleeper_league_rosters",
        "description": "Get the raw league data for a given Sleeper league ID. Returns the league object as returned by the Sleeper API.",
        "inputSchema": {
            "type": "object",
            "properties": {"league_id": {"title": "League Id", "type": "string"}},
            "required": ["league_id"],
        },
        "outputSchema": {
            "type": "object",
            "properties": {
                "result": {
                    "items": {"additionalProperties": true, "type": "object"},
                    "title": "Result",
                    "type": "array",
                }
            },
            "required": ["result"],
            "title": "_WrappedResult",
            "x-fastmcp-wrap-result": true,
        },
        "_meta": {"_fastmcp": {"tags": []}},
    },
    {
        "name": "get_sleeper_league_users",
        "description": "Get the users for a given Sleeper league ID. Returns a list of user objects as returned by the Sleeper API.",
        "inputSchema": {
            "type": "object",
            "properties": {"league_id": {"title": "League Id", "type": "string"}},
            "required": ["league_id"],
        },
        "outputSchema": {
            "type": "object",
            "properties": {
                "result": {
                    "items": {"additionalProperties": true, "type": "object"},
                    "title": "Result",
                    "type": "array",
                }
            },
            "required": ["result"],
            "title": "_WrappedResult",
            "x-fastmcp-wrap-result": true,
        },
        "_meta": {"_fastmcp": {"tags": []}},
    },
    {
        "name": "get_sleeper_league_matchups",
        "description": "Get the raw matchup data for a given Sleeper league ID and week. The caller must provide the target week.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "league_id": {"title": "League Id", "type": "string"},
                "week": {"title": "Week", "type": "integer"},
            },
            "required": ["league_id", "week"],
        },
        "outputSchema": {
            "type": "object",
            "properties": {
                "result": {
                    "items": {"additionalProperties": true, "type": "object"},
                    "title": "Result",
                    "type": "array",
                }
            },
            "required": ["result"],
            "title": "_WrappedResult",
            "x-fastmcp-wrap-result": true,
        },
        "_meta": {"_fastmcp": {"tags": []}},
    },
    {
        "name": "get_sleeper_league_transactions",
        "description": "Get transactions for a given Sleeper league ID and week. Optionally filter by transaction type such as 'trade', 'waiver', or 'free_agent'.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "league_id": {"title": "League Id", "type": "string"},
                "week": {"title": "Week", "type": "integer"},
                "txn_type": {
                    "anyOf": [{"type": "string"}, {"type": "null"}],
                    "default": null,
                    "title": "Txn Type",
                },
            },
            "required": ["league_id", "week"],
        },
        "outputSchema": {
            "type": "object",
            "properties": {
                "result": {
                    "items": {"additionalProperties": true, "type": "object"},
                    "title": "Result",
                    "type": "array",
                }
            },
            "required": ["result"],
            "title": "_WrappedResult",
            "x-fastmcp-wrap-result": true,
        },
        "_meta": {"_fastmcp": {"tags": []}},
    },
    {
        "name": "get_sleeper_trending_players",
        "description": "Get trending players for the specified sport from Sleeper. Use add_drop to choose adds or drops, hours to set the lookback period, and limit for the number of players returned.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "sport": {"default": "nfl", "title": "Sport", "type": "string"},
                "add_drop": {"default": "add", "title": "Add Drop", "type": "string"},
                "hours": {"default": 24, "title": "Hours", "type": "integer"},
                "limit": {"default": 25, "title": "Limit", "type": "integer"},
            },
        },
        "outputSchema": {
            "type": "object",
            "properties": {
                "result": {
                    "items": {"additionalProperties": true, "type": "object"},
                    "title": "Result",
                    "type": "array",
                }
            },
            "required": ["result"],
            "title": "_WrappedResult",
            "x-fastmcp-wrap-result": true,
        },
        "_meta": {"_fastmcp": {"tags": []}},
    },
    {
        "name": "get_sleeper_user_drafts",
        "description": "Get all drafts for a Sleeper user. Provide the username and optionally sport and season. Returns a list of draft objects as returned by the Sleeper API.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "username": {"title": "Username", "type": "string"},
                "sport": {"default": "nfl", "title": "Sport", "type": "string"},
                "season": {"default": 2025, "title": "Season", "type": "integer"},
            },
            "required": ["username"],
        },
        "outputSchema": {
            "type": "object",
            "properties": {
                "result": {
                    "items": {"additionalProperties": true, "type": "object"},
                    "title": "Result",
                    "type": "array",
                }
            },
            "required": ["result"],
            "title": "_WrappedResult",
            "x-fastmcp-wrap-result": true,
        },
        "_meta": {"_fastmcp": {"tags": []}},
    },
    {
        "name": "get_sleeper_league_by_id",
        "description": "Get a Sleeper league by its ID. Includes basic info, scoring settings, league settings, and roster positions.",
        "inputSchema": {
            "type": "object",
            "properties": {"league_id": {"title": "League Id", "type": "string"}},
            "required": ["league_id"],
        },
        "outputSchema": {"type": "object", "additionalProperties": true},
        "_meta": {"_fastmcp": {"tags": []}},
    },
    {
        "name": "get_sleeper_draft_by_id",
        "description": "Get a Sleeper draft by its ID. Includes basic info, participants, and draft settings.",
        "inputSchema": {
            "type": "object",
            "properties": {"draft_id": {"title": "Draft Id", "type": "string"}},
            "required": ["draft_id"],
        },
        "outputSchema": {"type": "object", "additionalProperties": true},
        "_meta": {"_fastmcp": {"tags": []}},
    },
    {
        "name": "get_sleeper_all_draft_picks_by_id",
        "description": "Get all draft picks for a given Sleeper draft ID.",
        "inputSchema": {
            "type": "object",
            "properties": {"draft_id": {"title": "Draft Id", "type": "string"}},
            "required": ["draft_id"],
        },
        "outputSchema": {"type": "object", "additionalProperties": true},
        "_meta": {"_fastmcp": {"tags": []}},
    },
    {
        "name": "get_dictionary_info",
        "description": "Fetch rows from the combined dictionary view, optionally filtering by search criteria in the description. Parameter: search_criteria (list[str], optional).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "search_criteria": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Search Criteria",
                }
            },
        },
        "outputSchema": {
            "type": "object",
            "properties": {
                "result": {
                    "items": {"additionalProperties": true, "type": "object"},
                    "title": "Result",
                    "type": "array",
                }
            },
            "required": ["result"],
            "title": "_WrappedResult",
            "x-fastmcp-wrap-result": true,
        },
        "_meta": {"_fastmcp": {"tags": []}},
    },
    {
        "name": "get_metrics_metadata",
        "description": "Returns metric definitions by category for receiving, passing, rushing, and defense advanced NFL statistics. Use subcategory to pick one of: basic_info, volume_metrics, efficiency_metrics, situational_metrics, weekly.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "category": {
                    "anyOf": [{"type": "string"}, {"type": "null"}],
                    "default": null,
                    "title": "Category",
                },
                "subcategory": {
                    "anyOf": [{"type": "string"}, {"type": "null"}],
                    "default": null,
                    "title": "Subcategory",
                },
            },
        },
        "outputSchema": {"type": "object", "additionalProperties": true},
        "_meta": {"_fastmcp": {"tags": []}},
    },
    {
        "name": "get_advanced_receiving_stats",
        "description": "\n        Fetch advanced seasonal receiving stats for NFL players.\n\n        - Optional filters: player_names (partial matches), season_list, metrics.\n        - Optional controls: order_by_metric (sort DESC), limit (default 100, capped by implementation), positions (defaults to ['WR','TE','RB']).\n        - Safety: fully-unfiltered queries (no name/season/position) are refused unless allow_unfiltered=True.\n\n        For detailed metric definitions and categories, use the get_metrics_metadata tool.\n\n        Volume Metrics: (workhorse, production, usage)\n        games, targets, receptions, receiving_yards, receiving_tds, fantasy_points, fantasy_points_ppr, air_yards_share, receiving_air_yards, receiving_first_downs, receiving_2pt_conversions, receiving_yards_after_catch, gs, td, ybc, yds, team_abbr, player_position, height, weight\n        \n        Efficiency Metrics: (how well a player converted their opportunities)\n        dom, racr, ay_sh, ry_sh, w8dom, ppr_sh, rfd_sh, rtd_sh, tgt_sh, wopr_x, wopr_y, yac_sh, yptmpa, rtdfd_sh, target_share, receiving_epa, receiving_tds, int, rat, x1d, adot, yac_r, ybc_r, rec_br, brk_tkl, drop_percent, avg_yac, avg_expected_yac, catch_percentage, avg_intended_air_yards, avg_yac_above_expectation, percent_share_of_intended_air_yards\n        \n        Situational/Advanced Metrics: (what situations/roles, context stats)\n        receiving_2pt_conversions, receiving_first_downs, avg_cushion, avg_separation, player_display_name, receiving_yards_after_catch, age, drop\n        \n        Basic player info (season, player_name, ff_team, merge_name) is always included.\n        ",
        "inputSchema": {
            "type": "object",
            "properties": {
                "player_names": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Player Names",
                },
                "season_list": {
                    "anyOf": [
                        {"items": {"type": "integer"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Season List",
                },
                "metrics": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Metrics",
                },
                "order_by_metric": {
                    "anyOf": [{"type": "string"}, {"type": "null"}],
                    "default": null,
                    "title": "Order By Metric",
                },
                "limit": {
                    "anyOf": [{"type": "integer"}, {"type": "null"}],
                    "default": 100,
                    "title": "Limit",
                },
                "positions": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Positions",
                },
            },
        },
        "outputSchema": {"type": "object", "additionalProperties": true},
        "_meta": {"_fastmcp": {"tags": []}},
    },
    {
        "name": "get_advanced_passing_stats",
        "description": "\n        Fetch advanced seasonal passing stats for NFL quarterbacks and passers.\n        - Optional filters: player_names (partial matches), season_list, metrics.\n        - Optional controls: order_by_metric (sort DESC), limit (default 100, capped by implementation), positions (defaults to ['QB']).\n        - Query by player names, season, and choose which metrics to include by category or individually.\n        - Supports three metric categories: Volume, Efficiency, and Situational/Advanced.\n\n        Volume Metrics: (production, usage, and play counts)\n        qb_plays, times_hit, times_sacked, times_blitzed, times_hurried, times_pressured, exp_sack, passing_drops, receiving_drop, def_times_hitqb, def_times_blitzed, def_times_hurried\n\n        Efficiency Metrics: (conversion rates, accuracy, and advanced efficiency)\n        passer_rating, completion_percentage, avg_air_distance, avg_intended_air_yards, avg_air_yards_to_sticks, avg_completed_air_yards, avg_air_yards_differential, max_air_distance, max_completed_air_distance, expected_completion_percentage, completion_percentage_above_expectation, qbr_raw, qbr_total, qbr_rank, epa_total, times_pressured_pct\n\n        Situational/Advanced Metrics: (pressure, turnover, and contextual passing stats)\n        aggressiveness, avg_time_to_throw, passing_bad_throws, passing_bad_throw_pct, passing_drop_pct, receiving_drop_pct, pfr_player_id, pfr_player_name, merge_name, team, position, season, week, height, weight\n\n        For detailed metric definitions and categories, use the get_metrics_metadata tool.\n        Basic player info (season, week, player_name, team, position, merge_name, height, weight) is always included.\n        ",
        "inputSchema": {
            "type": "object",
            "properties": {
                "player_names": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Player Names",
                },
                "season_list": {
                    "anyOf": [
                        {"items": {"type": "integer"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Season List",
                },
                "metrics": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Metrics",
                },
                "order_by_metric": {
                    "anyOf": [{"type": "string"}, {"type": "null"}],
                    "default": null,
                    "title": "Order By Metric",
                },
                "limit": {
                    "anyOf": [{"type": "integer"}, {"type": "null"}],
                    "default": 100,
                    "title": "Limit",
                },
                "positions": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Positions",
                },
            },
        },
        "outputSchema": {"type": "object", "additionalProperties": true},
        "_meta": {"_fastmcp": {"tags": []}},
    },
    {
        "name": "get_advanced_rushing_stats",
        "description": "\n        Fetch advanced seasonal rushing stats for NFL running backs, hybrid backs, and runners.\n        - Optional filters: player_names (partial matches), season_list, metrics.\n        - Optional controls: order_by_metric (sort DESC), limit (default 100, capped by implementation), positions (defaults to ['RB','QB']).\n        - Query by player names, season, and choose which metrics to include by category or individually.\n        - Supports three metric categories: Volume, Efficiency, and Situational/Advanced.\n\n        Volume Metrics: (production, usage, and play counts)\n        games, carries, rushing_yards, rushing_tds, rushing_first_downs, targets, receptions, receiving_yards, receiving_tds, rush_attempts, rush_touchdowns, gs, td, yds, att\n\n        Efficiency Metrics: (rate stats and advanced context)\n        dom, ry_sh, w8dom, ppr_sh, yac_sh, yptmpa, rushing_epa, receiving_epa, target_share, fantasy_points, fantasy_points_ppr, rushing_fumbles, rushing_fumbles_lost, rushing_yards_after_catch, receiving_yards_after_catch, att_br, brk_tkl, yac, ybc, yac_att, ybc_att, avg_rush_yards, efficiency, expected_rush_yards, rush_pct_over_expected, rush_yards_over_expected, rush_yards_over_expected_per_att, percent_attempts_gte_eight_defenders, avg_time_to_los\n\n        Situational/Advanced Metrics: (goal-line, context, and next-level situational stats)\n        rushing_2pt_conversions, receiving_2pt_conversions, rushing_first_downs, x1d, age, rushing_yards_after_catch\n\n        For detailed metric definitions and categories, use the get_metrics_metadata tool.\n        Basic player info (season, player_name, ff_team, merge_name) is always included.\n        ",
        "inputSchema": {
            "type": "object",
            "properties": {
                "player_names": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Player Names",
                },
                "season_list": {
                    "anyOf": [
                        {"items": {"type": "integer"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Season List",
                },
                "metrics": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Metrics",
                },
                "order_by_metric": {
                    "anyOf": [{"type": "string"}, {"type": "null"}],
                    "default": null,
                    "title": "Order By Metric",
                },
                "limit": {
                    "anyOf": [{"type": "integer"}, {"type": "null"}],
                    "default": 100,
                    "title": "Limit",
                },
                "positions": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Positions",
                },
            },
        },
        "outputSchema": {"type": "object", "additionalProperties": true},
        "_meta": {"_fastmcp": {"tags": []}},
    },
    {
        "name": "get_advanced_defense_stats",
        "description": "\n        Fetch advanced seasonal defensive stats for NFL defenders and defensive playmakers.\n\n        - Optional filters: player_names (partial matches), season_list, metrics.\n        - Optional controls: order_by_metric (sort DESC), limit (default 100, capped by implementation), positions (defaults to ['CB','DB','DE','DL','LB','S']).\n        - Query by player names, season, and choose which metrics to include by category or individually.\n        - Supports three metric categories: Volume, Efficiency, and Situational/Advanced.\n\n        Volume Metrics: (production, usage, and appearance counts)\n        g, gs, sk, td, air, cmp, int, tgt, prss, bltz, hrry, qbkd, comb, m_tkl, loaded\n\n        Efficiency Metrics: (coverage, tackling, and pressure rates)\n        cmp_percent, m_tkl_percent, yds_cmp, yds_tgt, rat, yds, yac\n\n        Situational/Advanced Metrics: (contextual and advanced defensive stats)\n        dadot, age, pos, pfr_id, gsis_id, merge_name, team, player_name, height, weight\n\n        For detailed metric definitions and categories, use the get_metrics_metadata tool.\n        Basic player info (season, week, player_name, team, position, merge_name, height, weight) is always included.\n        ",
        "inputSchema": {
            "type": "object",
            "properties": {
                "player_names": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Player Names",
                },
                "season_list": {
                    "anyOf": [
                        {"items": {"type": "integer"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Season List",
                },
                "metrics": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Metrics",
                },
                "order_by_metric": {
                    "anyOf": [{"type": "string"}, {"type": "null"}],
                    "default": null,
                    "title": "Order By Metric",
                },
                "limit": {
                    "anyOf": [{"type": "integer"}, {"type": "null"}],
                    "default": 100,
                    "title": "Limit",
                },
                "positions": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Positions",
                },
            },
        },
        "outputSchema": {"type": "object", "additionalProperties": true},
        "_meta": {"_fastmcp": {"tags": []}},
    },
    {
        "name": "get_advanced_receiving_stats_weekly",
        "description": "\n        Fetch advanced weekly receiving stats for NFL players.\n\n        - Optional filters: player_names (partial matches), season_list, weekly_list, metrics.\n        - Optional controls: order_by_metric (sort DESC), limit (default 100, capped by implementation), positions (defaults to ['WR','TE','RB']).\n        - Query by player names, season, week, and choose which metrics to include by category or individually.\n        - Supports three metric categories: Volume, Efficiency, and Situational/Advanced.\n\n        Volume Metrics: (workhorse, production, usage)\n        passing_drops, receiving_int, receiving_drop, rushing_broken_tackles, receiving_broken_tackles\n\n        Efficiency Metrics: (conversion, catch rates, and advanced context)\n        receiving_rat, passing_drop_pct, receiving_drop_pct, avg_yac, avg_expected_yac, catch_percentage, avg_intended_air_yards, avg_yac_above_expectation, percent_share_of_intended_air_yards\n\n        Situational/Advanced Metrics: (separation, context, and team info)\n        avg_cushion, avg_separation, player_position, player_display_name, ngr_team\n\n        For detailed metric definitions and categories, use the get_metrics_metadata tool.\n        Basic player info (season, week, player_name, ff_team, ff_position, merge_name, height, weight) is always included.\n        ",
        "inputSchema": {
            "type": "object",
            "properties": {
                "player_names": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Player Names",
                },
                "season_list": {
                    "anyOf": [
                        {"items": {"type": "integer"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Season List",
                },
                "weekly_list": {
                    "anyOf": [
                        {"items": {"type": "integer"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Weekly List",
                },
                "metrics": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Metrics",
                },
                "order_by_metric": {
                    "anyOf": [{"type": "string"}, {"type": "null"}],
                    "default": null,
                    "title": "Order By Metric",
                },
                "limit": {
                    "anyOf": [{"type": "integer"}, {"type": "null"}],
                    "default": 100,
                    "title": "Limit",
                },
                "positions": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Positions",
                },
            },
        },
        "outputSchema": {"type": "object", "additionalProperties": true},
        "_meta": {"_fastmcp": {"tags": []}},
    },
    {
        "name": "get_advanced_passing_stats_weekly",
        "description": "\n        Fetch advanced weekly passing stats for NFL quarterbacks and passers.\n\n        - Optional filters: player_names (partial matches), season_list, weekly_list, metrics.\n        - Optional controls: order_by_metric (sort DESC), limit (default 100, capped by implementation), positions (defaults to ['QB']).\n        - Query by player names, season, week, and choose which metrics to include by category or individually.\n        - Supports three metric categories: Volume, Efficiency, and Situational/Advanced.\n\n        Volume Metrics: (production, usage, and play counts)\n        qb_plays, times_hit, times_sacked, times_blitzed, times_hurried, times_pressured, exp_sack, passing_drops, receiving_drop, def_times_hitqb, def_times_blitzed, def_times_hurried\n\n        Efficiency Metrics: (conversion rates, accuracy, and advanced efficiency)\n        passer_rating, completion_percentage, avg_air_distance, avg_intended_air_yards, avg_air_yards_to_sticks, avg_completed_air_yards, avg_air_yards_differential, max_air_distance, max_completed_air_distance, expected_completion_percentage, completion_percentage_above_expectation, qbr_raw, qbr_total, qbr_rank, epa_total, times_pressured_pct\n\n        Situational/Advanced Metrics: (pressure, turnover, and contextual passing stats)\n        aggressiveness, avg_time_to_throw, passing_bad_throws, passing_bad_throw_pct, passing_drop_pct, receiving_drop_pct, pfr_player_id, pfr_player_name, merge_name, team, position, season, week, height, weight\n\n        For detailed metric definitions and categories, use the get_metrics_metadata tool.\n        Basic player info (season, week, player_name, team, position, merge_name, height, weight) is always included.\n        ",
        "inputSchema": {
            "type": "object",
            "properties": {
                "player_names": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Player Names",
                },
                "season_list": {
                    "anyOf": [
                        {"items": {"type": "integer"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Season List",
                },
                "weekly_list": {
                    "anyOf": [
                        {"items": {"type": "integer"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Weekly List",
                },
                "metrics": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Metrics",
                },
                "order_by_metric": {
                    "anyOf": [{"type": "string"}, {"type": "null"}],
                    "default": null,
                    "title": "Order By Metric",
                },
                "limit": {
                    "anyOf": [{"type": "integer"}, {"type": "null"}],
                    "default": 100,
                    "title": "Limit",
                },
                "positions": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Positions",
                },
            },
        },
        "outputSchema": {"type": "object", "additionalProperties": true},
        "_meta": {"_fastmcp": {"tags": []}},
    },
    {
        "name": "get_advanced_rushing_stats_weekly",
        "description": "\n        Fetch advanced weekly rushing stats for NFL running backs, hybrid backs, and runners.\n        - Optional filters: player_names (partial matches), season_list, weekly_list, metrics.\n        - Optional controls: order_by_metric (sort DESC), limit (default 100, capped by implementation), positions (defaults to ['RB','QB']).\n        - Query by player names, season, week, and choose which metrics to include by category or individually.\n        - Supports three metric categories: Volume, Efficiency, and Situational/Advanced.\n\n        Volume Metrics: (production, usage, and play counts)\n        rush_attempts, rush_touchdowns\n\n        Efficiency Metrics: (rate stats and advanced context)\n        efficiency, avg_rush_yards, avg_time_to_los, expected_rush_yards, rush_pct_over_expected, rush_yards_over_expected, rush_yards_over_expected_per_att, percent_attempts_gte_eight_defenders\n\n        Situational/Advanced Metrics: (broken tackles, contact, and context)\n        rushing_broken_tackles, receiving_broken_tackles, rushing_yards_after_contact, rushing_yards_before_contact, rushing_yards_after_contact_avg, rushing_yards_before_contact_avg\n\n        For detailed metric definitions and categories, use the get_metrics_metadata tool.\n        Basic player info (season, week, player_name, team, position, merge_name, height, weight) is always included.\n        ",
        "inputSchema": {
            "type": "object",
            "properties": {
                "player_names": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Player Names",
                },
                "season_list": {
                    "anyOf": [
                        {"items": {"type": "integer"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Season List",
                },
                "weekly_list": {
                    "anyOf": [
                        {"items": {"type": "integer"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Weekly List",
                },
                "metrics": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Metrics",
                },
                "order_by_metric": {
                    "anyOf": [{"type": "string"}, {"type": "null"}],
                    "default": null,
                    "title": "Order By Metric",
                },
                "limit": {
                    "anyOf": [{"type": "integer"}, {"type": "null"}],
                    "default": 100,
                    "title": "Limit",
                },
                "positions": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Positions",
                },
            },
        },
        "outputSchema": {"type": "object", "additionalProperties": true},
        "_meta": {"_fastmcp": {"tags": []}},
    },
    {
        "name": "get_advanced_defense_stats_weekly",
        "description": "\n        Fetch advanced weekly defensive stats for NFL defenders and defensive playmakers.\n        - Optional filters: player_names (partial matches), season_list, weekly_list, metrics.\n        - Optional controls: order_by_metric (sort DESC), limit (default 100, capped by implementation), positions (defaults to ['CB','DB','DE','DL','LB','S']).\n        - Query by player names, season, week, and choose which metrics to include by category or individually.\n        - Supports three metric categories: Volume, Efficiency, and Situational/Advanced.\n\n        Volume Metrics: (production, usage, and appearance counts)\n        def_tackles_combined, def_sacks, def_ints, def_targets, def_pressures, def_times_blitzed, def_times_hurried, def_times_hitqb\n\n        Efficiency Metrics: (coverage, tackling, and pressure rates)\n        def_completion_pct, def_missed_tackles, def_missed_tackle_pct, def_completions_allowed, def_yards_allowed, def_yards_allowed_per_cmp, def_yards_allowed_per_tgt, def_passer_rating_allowed\n\n        Situational/Advanced Metrics: (contextual and advanced defensive stats)\n        def_adot, def_yards_after_catch, def_air_yards_completed, def_receiving_td_allowed, game_id, game_type, opponent, pfr_game_id, pfr_player_id, pfr_player_name\n\n        For detailed metric definitions and categories, use the get_metrics_metadata tool.\n        Basic player info (season, week, player_name, team, position, merge_name, height, weight) is always included.\n        ",
        "inputSchema": {
            "type": "object",
            "properties": {
                "player_names": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Player Names",
                },
                "season_list": {
                    "anyOf": [
                        {"items": {"type": "integer"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Season List",
                },
                "weekly_list": {
                    "anyOf": [
                        {"items": {"type": "integer"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Weekly List",
                },
                "metrics": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Metrics",
                },
                "order_by_metric": {
                    "anyOf": [{"type": "string"}, {"type": "null"}],
                    "default": null,
                    "title": "Order By Metric",
                },
                "limit": {
                    "anyOf": [{"type": "integer"}, {"type": "null"}],
                    "default": 100,
                    "title": "Limit",
                },
                "positions": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Positions",
                },
            },
        },
        "outputSchema": {"type": "object", "additionalProperties": true},
        "_meta": {"_fastmcp": {"tags": []}},
    },
    {
        "name": "get_stats_metadata",
        "description": "Return game-stat field definitions for NFL offense/defense. Category: 'offense'|'defense' (aliases: 'off','o','def','d'). Offense subcategories: overall, passing, rushing, receiving, pressure_and_sacks, special_teams, seasonal. Defense subcategories: overall, tackling, pressure, coverage, turnovers, penalties. Case-insensitive; omit subcategory to return full category.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "category": {"title": "Category", "type": "string"},
                "subcategory": {
                    "anyOf": [{"type": "string"}, {"type": "null"}],
                    "default": null,
                    "title": "Subcategory",
                },
            },
            "required": ["category"],
        },
        "outputSchema": {"type": "object", "additionalProperties": true},
        "_meta": {"_fastmcp": {"tags": []}},
    },
    {
        "name": "get_offensive_players_game_stats",
        "description": "\n        Fetch offensive weekly game stats for NFL players.\n\n        Optional filters:\n        - player_names: list of partial/full player name strings to match (case-insensitive partial matching supported).\n        - season_list: list of seasons (ints) to restrict results to specific years.\n        - weekly_list: list of week numbers (ints) to restrict results to specific game weeks.\n        - metrics: list of metric names to include; if omitted a default set of core offensive metrics is returned.\n\n        Controls:\n        - order_by_metric: metric name to sort results by (descending).\n        - limit: maximum number of rows to return (default 100; implementation may enforce a maximum cap).\n        - positions: list of offensive positions to include (defaults to typical offensive roles, e.g. ['QB', 'RB', 'WR', 'TE']).\n\n        Behavior and notes:\n        - This function returns per-game (weekly) offensive statistics suitable for tools and agents; basic player info (season, week, player_name, team, position, merge_name, height, weight) is always included.\n        - Typical metric categories available include:\n            - Volume: passing yards, rushing yards, receiving yards, touchdowns, targets, snaps.\n            - Efficiency/context: completion percentage, yards per attempt, yards after catch, missed tackle rate.\n            - Situational/advanced: red zone efficiency, third down conversion rate, game identifiers, opponent, and other contextual fields.\n        - For safety and performance, fully unfiltered queries (no player_names, season_list, weekly_list, or positions specified) may be refused or limited by the implementation; prefer narrowing queries by name, season, week, or position.\n        - Returns: dict containing the queried rows and any metadata or error information.\n        ",
        "inputSchema": {
            "type": "object",
            "properties": {
                "player_names": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Player Names",
                },
                "season_list": {
                    "anyOf": [
                        {"items": {"type": "integer"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Season List",
                },
                "weekly_list": {
                    "anyOf": [
                        {"items": {"type": "integer"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Weekly List",
                },
                "metrics": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Metrics",
                },
                "order_by_metric": {
                    "anyOf": [{"type": "string"}, {"type": "null"}],
                    "default": null,
                    "title": "Order By Metric",
                },
                "limit": {
                    "anyOf": [{"type": "integer"}, {"type": "null"}],
                    "default": 100,
                    "title": "Limit",
                },
                "positions": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Positions",
                },
            },
        },
        "outputSchema": {"type": "object", "additionalProperties": true},
        "_meta": {"_fastmcp": {"tags": []}},
    },
    {
        "name": "get_defensive_players_game_stats",
        "description": "\n        Fetch defensive weekly game stats for NFL players.\n\n        Optional filters:\n        - player_names: list of partial/full player name strings to match (case-insensitive partial matching supported).\n        - season_list: list of seasons (ints) to restrict results to specific years.\n        - weekly_list: list of week numbers (ints) to restrict results to specific game weeks.\n        - metrics: list of metric names to include; if omitted a default set of core defensive metrics is returned.\n\n        Controls:\n        - order_by_metric: metric name to sort results by (descending).\n        - limit: maximum number of rows to return (default 100; implementation may enforce a maximum cap).\n        - positions: list of defensive positions to include (defaults to typical defensive roles, e.g. ['CB', 'DB', 'DE', 'DL', 'LB', 'S']).\n\n        Behavior and notes:\n        - This function returns per-game (weekly) defensive statistics suitable for tools and agents; basic player info (season, week, player_name, team, position, merge_name, height, weight) is always included.\n        - Typical metric categories available include:\n            - Volume: tackles, assisted tackles, sacks, interceptions, targets, pressures, pass breakups.\n            - Efficiency/context: completion percentage allowed, yards allowed, yards per target, passer rating allowed, missed tackle rate.\n            - Situational/advanced: yards after catch allowed, air yards completed, receiving TDs allowed, game identifiers, opponent, and other contextual fields.\n        - For safety and performance, fully unfiltered queries (no player_names, season_list, weekly_list, or positions specified) may be refused or limited by the implementation; prefer narrowing queries by name, season, week, or position.\n        - Returns: dict containing the queried rows and any metadata or error information.\n        ",
        "inputSchema": {
            "type": "object",
            "properties": {
                "player_names": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Player Names",
                },
                "season_list": {
                    "anyOf": [
                        {"items": {"type": "integer"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Season List",
                },
                "weekly_list": {
                    "anyOf": [
                        {"items": {"type": "integer"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Weekly List",
                },
                "metrics": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Metrics",
                },
                "order_by_metric": {
                    "anyOf": [{"type": "string"}, {"type": "null"}],
                    "default": null,
                    "title": "Order By Metric",
                },
                "limit": {
                    "anyOf": [{"type": "integer"}, {"type": "null"}],
                    "default": 100,
                    "title": "Limit",
                },
                "positions": {
                    "anyOf": [
                        {"items": {"type": "string"}, "type": "array"},
                        {"type": "null"},
                    ],
                    "default": null,
                    "title": "Positions",
                },
            },
        },
        "outputSchema": {"type": "object", "additionalProperties": true},
        "_meta": {"_fastmcp": {"tags": []}},
    },
]
